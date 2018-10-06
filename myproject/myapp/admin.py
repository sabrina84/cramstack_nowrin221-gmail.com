from django.contrib import admin

from .models import UserInfo, contactInfo

admin.site.register(UserInfo)
admin.site.register(contactInfo)