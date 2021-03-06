from django.db import models
from movecar.models import User

# Create your models here.

class User_info(models.Model):
    id = models.BigAutoField(primary_key=True, blank=True)
    openid = models.CharField(max_length=32, null=True, blank=True)
    unionid = models.CharField(max_length=32, null=True, blank=True)
    nickname = models.CharField(max_length=32, blank=True, null=True)
    sex = models.BooleanField(default=0, blank=True)
    province = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    headimgurl = models.TextField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=8,null=True,blank=True)
    privilege = models.TextField(max_length=255, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

