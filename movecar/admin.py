from django.contrib import admin
from .models import User, Inquire, User_addr


admin.site.register(User)
admin.site.register(Inquire)
admin.site.register(User_addr)

