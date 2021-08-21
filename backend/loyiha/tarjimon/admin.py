from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import Lugat

class LugatAdmin(admin.ModelAdmin):
    list_display = ['inglizcha', 'uzbekcha']
class LugatAdmin(admin.ModelAdmin):
    admin.site.register(Lugat, LugatAdmin)
