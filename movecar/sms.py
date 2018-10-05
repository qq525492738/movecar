import json
from urllib import parse, request


def sms(types="xsend", phone="15877752003", var={'code': '5254'}, template="Verification"):
    templates = {"Message": "fVuFA3", "Verification": "h4jH73"}

    project = templates.get(template, "h4jH73")

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

    appid = "23363"
    appkey = "4012447e232c0db3ff223fddaecebe7d"
    
    data = {
        "appid": appid,
        "signature": appkey
        }
    
    var = json.dumps(var)

    if types == "xsend":
        data["project"] = project
        data["to"] = phone
        data["vars"] = var
        
    elif types == "send":
        data["to"] = phone
        if not ("【钉钉墙】" in var):
            var = "【钉钉墙】" + var
        data["content"] = var
        
    elif types == "multi":
        data["project"] = project
        data["multi"] = var

    url="https://api.mysubmail.com/message/" + types
    data = parse.urlencode(data).encode("utf-8")
    req = request.urlopen(url=url, data=data)
    return req.read().decode("utf-8")


if __name__ == '__main__':
    print(sms(var={'code': 525492}))

