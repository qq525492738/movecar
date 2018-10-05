from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, Http404, HttpResponseServerError
from .models import User, Inquire, User_addr
from django.views import generic
from .sms import sms
import random
from .call import Phone
import json
from wechat_service.wechat_template import Templates_message
from django.shortcuts import render, redirect
from wechat_service import message as ms
from wechat_service.basic import Basic
from wechat_service.views import WechatApiView, GetUserInfo
from django.views.generic import View
from . import wechat_api


def ssl(request):
    return HttpResponse("201808310000003ck5fllqdym2b0xhgsm5eee3i42eevg89zme0k136svu4k2zkg")



def verify(request):
    return HttpResponse("WUPZbZ5M3JyEfpYE")


def index(request):
    if request.method == 'GET':
        id = request.session.get('id',None)

        if id:
            return render(request,'index.html')
        else:
            ms.log('index else')
            return redirect('wechat_service', path="index")

            
def center(request):
    id= request.session.get('id',None)
    if id:
        ms.log("center--id == True id="+str(id))
        try:
            user = User.objects.get(id=id)
            headimgurl = user.user_info.headimgurl
            nickname = user.user_info.nickname
            return render(request, 'center.html', {'headimgurl': headimgurl,'nickname':nickname,'phone': user.phone, 'license_plate': user.license_plate})
        except:
            return render(request, 'center.html', {'headimgurl':'static/img/logo.png','nickname':'请先点击头像登录','phone': '请先登录', 'license_plate': '请先登录'})
    else: 
        ms.log("center-->return redirect")
        return redirect('wechat_service', path="center")


def bind_phone(request):
    ms.log("request method="+request.method)
    if request.method == 'POST':
        #vc = request.POST.get('vc')
        p = request.POST.get("p")

        #if str(request.session.get('vc', 0)) == vc:
        id = request.session.get('id','')
        if id:
            user= User.objects.get(id=id)
            if not(user.phone) or user.phone != p:
                user.phone = p
                user.save()
            return redirect('index')
            
        else:
            return redirect('wechat_service', path="index")

    if request.method == 'GET':
        return render(request,'login.html')

            

def user_addr(request):
    if request.method == "POST":
        addr = request.POST.get('addr')
        p = request.POST.get('p')
        if addr and p:
            try:
                id = request.session.get('id')
                if not(id):
                    return render(request, 'prompt.html', {'prompt': '请求错误,请先登录'})

                user = User.objects.get(id=id)
                User_addr.objects.create(addr=addr, user=user).save()
                return render(request, 'prompt.html', {'prompt': "申请成功,挪车码会通过快递方法发给您"})
            except User.DoesNotExist:
                return render(request, 'prompt.html', {'prompt': '请求错误,请先绑定车牌'})
        else:
            return render(request, 'prompt.html', {'prompt': "请求错误"})

def inquire_virtual_phone(request):
    if request.method == "POST":
        id = request.session.get('id')

        if not(id):
            return JsonResponse({'code': '40005', 'errmsg': 'license plate does not exist'})
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return JsonResponse({'code': '40005', 'errmsg': 'license plate does not exist'})
        
        if user.phone==None:
            return JsonResponse({'code': '40011', 'errmsg': 'please login'})

        tela = user.phone
        lp = request.POST.get("lp")

        try:
            callees = User.objects.filter(license_plate=lp.upper())
            if callees.count():
                callee = callees.reverse()[0]
            else:
                return JsonResponse({'code': '40404', 'errmsg': 'license plate does not exist'})

            telb = callee.phone
            inquire = Inquire.objects.create(caller_phone=tela, callee_phone=telb, inquire=user)
            phone = Phone()
            telx = phone.bind(tela=tela, telb=telb, requestid=str(inquire.id))
            inquire.middle_phone=telx
            inquire.save()
            #wt = Templates_message()
            #td = {
            #    "key": "value"
            #}
            #wt.send(access_token=Basic().get_access_token(), openid= user.openid, template_id= ti, template_data= td, url='https://www.yqzql.cn/wechat_service')
            return JsonResponse({'code': 0, 'errmsg': 'ok', 'data': telx})
        except User.DoesNotExist:
            return JsonResponse({'code': '40004', 'errmsg': 'user does not exist'})


def verifycode(request):
    if request.method == 'POST':
        code = random.randint(1000, 9999)
        p = request.POST.get('p')
        request.session['p'] = p
        request.session['vc'] = code
        if p:
            sms(phone=p, var={"code": code})
            return JsonResponse({"vc": code})  #最后改为返回 successfully
        else:
            return JsonResponse({'vc':'0'})



def bind_api(request):
    if request.method == 'POST':
        
        #code = request.POST.get('vc')
        p = request.POST.get("p")
        lp = request.POST.get("lp").upper()
        id = request.session.get('id')
        ms.log(p+lp+str(id))
        if not(id):
            render(request,'prompt.html',{'prompt':'请先登录 '})

        #if str(request.session.get('vc', 0)) == str(code):
        if True:
            if not (p and lp):
                return JsonResponse({'code': 40020, 'errsmg': 'agrs error'})
            try:
                user = User.objects.get(id=id)
                #user=User.objects.get_or_create(id=id, defaults={'phone': p, 'license_plate': lp})
                user.phone = p
                user.license_plate = lp
                user.save()
            except User.DoesNotExist:
                return JsonResponse({'code': 40011, 'errsmg': 'pleas bind phone'})
                #return render(request, 'prompt.html', {"prompt": "请先绑定手机号码"})

            #return render(request, 'prompt.html', {"prompt": "绑定成功"})
            ms.log('bind_api')
            return JsonResponse({'code': 0, 'errsmg': 'ok'})
        else:
            return render(request, 'prompt.html', {"prompt": "验证码错误"})
            #return JsonResponse({'code': 40018, 'errsmg': 'verify code error'})


class user_info(WechatApiView):
    def get(self, request):
        redir_url = request.path
        code = request.GET.get('code')

        if redir_url and code:
            token_data, error = self.wechat_api.get_auth_access_token(code)
            if error:
                wx_log_error(error)
                return HttpResponseServerError('get access_token error')
            user = self._save_user(user_info)
            if not user:
                return HttpResponseServerError('save userinfo error')

            request.session['user'] = user
            return redirect(redir_url)
        else:
            return Http404('parameter path or code not founded!!')
