from django.db import models
import uuid


class User(models.Model):
    id = models.BigAutoField(primary_key=True, blank=True)
    openid = models.CharField(max_length=32,null=True, blank=True)
    unionid = models.CharField(max_length=32,null=True, blank=True)
    username = models.CharField(max_length=32, blank=True, null=True)
    nickname = models.CharField(max_length=32, blank=True, null=True)
    phone = models.CharField(max_length=11,blank=True,null=True)
    license_plate = models.CharField(max_length=8,null=True ,blank=True)


class Inquire(models.Model):
    id = models.BigAutoField(primary_key=True, blank=True)
    caller_phone = models.CharField(max_length=11, blank=True, null=True)
    middle_phone = models.CharField(max_length=11, blank=True, null=True)
    callee_phone = models.CharField(max_length=11, blank=True, null=True)
    inquire = models.ForeignKey(User, on_delete=models.CASCADE)

class User_addr(models.Model):
    id = models.BigAutoField(primary_key=True, blank=True)
    addr = models.TextField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
