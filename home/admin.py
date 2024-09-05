from django.contrib import admin
from .models import CustumUser

class CustumUserAdmin(admin.ModelAdmin):
    list_display = ['name']  

admin.site.register(CustumUser, CustumUserAdmin)