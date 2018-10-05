from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseServerError
from django.views.generic import View
from . import auto, receive
import urllib, json
import hashlib
import simplejson
from django.urls import reverse
from movecar import settings as settings
from movecar.models import User
from .auth_view import AuthView as BaseView
from .wechat_api import WechatApi, wx_log_error
from django.core.mail import send_mail
from movecar.models import User

from .models import User_info
from . import message as ms




# Create your views here.

def verify(request):
	return HttpResponse('WUPZbZ5M3JyEfpYE')
class Reply(View):
    def get(request):
	    return HttpResponse(request.GET.get('echostr'))
    def post(request):
        return HttpResponse(auto.intelligent(receive.parse_xml(webData)).send())

class WechatApiView(View):
    APPID  = settings.APPID
    APPSECRET = settings.APPSECRET
    HOST = settings.HOST
    wechat_api = WechatApi(appid=APPID, appsecret=APPSECRET)

class AuthView(WechatApiView):
    def get(self, request):
        path= request.GET.get("path", "")
        code= request.GET.get("code", "")
        state= request.GET.get("state", '')
        relogin= request.GET.get("relogin", '')

        ms.log("path,"+path+" code,"+code+" state="+state)
        
        if path:
            ms.log(path)
            
            if 'id' in request.session and not relogin:
                ms.log("authview-->id in")
                return redirect(path)
            else:
                ms.log("authview-->if id in else")
                redirect_url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx1daf30a5ae26e09e&redirect_uri=https%3A%2F%2F{}{}&response_type=code&scope=snsapi_userinfo&state={}#wechat_redirect".format(self.HOST, request.path.replace("/","%2F"), path)
                ms.log(('auth_url'+redirect_url))
                return redirect(redirect_url)

        if code:
            wa= WechatApiView()
            token_data, err = wa.wechat_api.get_auth_access_token(code)
            if not err:
                openid = token_data.get("openid")
                user, err= User.objects.get_or_create(openid=openid, defaults={"openid": openid})
                GetUserInfo(access_token=token_data.get('access_token', ''), openid=openid)
                ms.log(str(type(user.id)))
                request.session['id'] = user.id
                return redirect(state)

            else:
                ms.log('authview-->'+str(err))
                return Http404('access_token error')
            
            
        else:
            return Http404('parameter path not found')


    
#def get_auth_code(self, request):
#    if request.path:
#        ms.log("auth_get_openid-->path-->" + request.path)
#        id = request.session.get("id",None)
#        if id not is None:
#            ms.log("auth_get_openid-->id in")
#            return redirect(request.path)
#        else:
#            #red_url = '%s%s?path=%s' % (self.HOST, reverse('wx:get_user_info'), path)
#            #redirect_url = self.wechat_api.auth_url(red_url)
#            redirect_url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx1daf30a5ae26e09e&redirect_uri=https%3A%2F%2Fyqzql.cn%2F{}&response_type=code&scope=snsapi_userinfo&state=123#wechat_redirect".format(request.path.replace("/","%2F"))
#            #redirect_url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx1daf30a5ae26e09e&redirect_uri=https%3A%2F%2Fyqzql.cn&response_type=code&scope=snsapi_base&state=123#wechat_redirect"
#            ms.log("auth_get_openid,redirect_url-->"+redirect_url)
#            return redirect(redirect_url)
#    else:
#        return Http404('parameter path not found')
#


	
def  GetUserInfo(access_token, openid):
    if access_token and openid:
        url = "https://api.weixin.qq.com/sns/userinfo?access_token={0}&openid={1}&lang=zh_CN".format(access_token, openid)
    else:
        return None

    res = urllib.request.urlopen(url=url)
    user_dict = json.loads(res.read().decode())
    openid = user_dict.get("openid",None)

    if openid:
        try:
            user = User.objects.get(openid=user_dict.get('openid'))
            user_dict['user']= user
            user_dict['sex'] -= 1
            ms.log(str(user_dict))
            user_info,err = User_info.objects.update_or_create(openid=user_dict.get('openid'),defaults=user_dict)
            user_info.save()
            ms.log(str(user_info))
            ms.log("user_info.save-->"+user_info.nickname)
            return user_dict
        except Exception as e:
            ms.log("wechat_view--.80->>"+str(e))
            return None

    else:
        return None


class TestView(BaseView):
    def get(self, request):
        return render(request, 'test.html')
