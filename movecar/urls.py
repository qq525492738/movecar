"""movecar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from .views import index, inquire_virtual_phone, verifycode, bind_api, center, user_addr#, AuthView, GetUserInfoView, TestView,  WxSignature
from .views import verify, bind_phone, ssl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('.well-known/pki-validation/fileauth.txt', ssl),
    path('index', index, name='index'),
    path('login', bind_phone, name='login'),
    path('bind_api', bind_api, name='bind_api'),
    path('verifycode', verifycode, name='verifycode'),
    path('inquire', inquire_virtual_phone, name='inquire'),
    path('center', center, name='center'),
    path('user_addr', user_addr, name='user_addr'),
    path('wechat_service', include('wechat_service.urls'), name='wechat_service'),
	path('MP_verify_WUPZbZ5M3JyEfpYE.txt', verify),
    #微信授权
#    path('auth', AuthView.as_view(), name='wx_auth'),
#    path('code', GetUserInfoView.as_view(), name='get_user_info'),
#    path('',WxSignature.as_view(), name='signature'),
#    path('test', TestView.as_view(), name='test_view'),
]
