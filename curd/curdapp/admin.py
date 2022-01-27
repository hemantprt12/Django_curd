from django.contrib import admin
from .models import UserDetails

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['User_Id','User_Name','User_Address']


admin.site.register(UserDetails,UserAdmin)