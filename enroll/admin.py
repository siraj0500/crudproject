from django.contrib import admin
# importing user class from models.py
from .models import User


# defining how the admin results should view by creating a class and the class should
# inherit from admin.ModelAdmin
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')


# Register your models here.
# (4) registering admin panel

admin.site.register(User,UserAdmin)
