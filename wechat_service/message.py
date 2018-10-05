#filename error
import smtplib,json
from email.mime.text import MIMEText
from email.header import Header
from urllib import request,parse
import time

def email(content = "error",subject = 'Automatic warning'):
    try:
        mail_host="smtp.qq.com"  
        mail_user="525492738@qq.com"    
        mail_pass="swxotobjqgavbibe"   

        sender = '525492738@qq.com'
        receivers = ['525492738@qq.com']  

        message = MIMEText(content, 'plain', 'utf-8')
        message['From'] = Header("525492738@qq.com", 'utf-8')
        message['To'] =  Header("525492738@qq.com", 'utf-8')

        message['Subject'] = Header(subject, 'utf-8')
         
        smtpObj = smtplib.SMTP_SSL(mail_host,465)
        smtpObj.set_debuglevel(1)
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())

    except:
        print("邮件发送出错")

def log(varible='err',filename='log'):
    with open('/var/www/html/django/movecar/'+str(filename), "a") as f:
        if isinstance(varible, int):
            varible = str(varible)
        f.write(time.strftime('%I:%M:%S')+"->"+varible+'\n')





def sms(types="xsend",phone="15877752003",var = {'code':'5254'},template="Verification"):
    templates = {"Message":"fVuFA3","Verification":"AkRjj1"}

    project = templates.get(template,"AkRjj1")

    """
 multi=[{
        "to":"15*********",
        "vars":{
            "name":"kevin",
            "code":123456
        }
    },{
        "to":"18*********",
        "vars":{
            "name":"jacky",
            "code":236554
        }
    },{
        "to":"13*********",
        "vars":{
            "name":"tom",
            "code":236554
        }]"""

    appid="17367"
    appkey="b9e8faf4eb99d70fc8d1d35e28dd74fb"
    
    data={
        "appid":appid,
        "signature":appkey
        }
    
    var = json.dumps(var)


    if types == "xsend":
        data["project"] = project
        data["to"] = phone
        data["vars"] = var
        
    elif types == "send":
        data["to"] = phone
        if not ("【一起赚钱啦】" in var):
            var = "【一起赚钱啦】" + var
        data["content"] = var
        
    elif types == "multi":
        data["project"] = project
        data["multi"] = var

    url="https://api.mysubmail.com/message/" + types
    data = parse.urlencode(data).encode("utf-8")
    req = request.urlopen(url=url,data=data)
    return req.read().decode("utf-8")


