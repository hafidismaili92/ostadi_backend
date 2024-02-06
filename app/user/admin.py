from django.contrib import admin

from user.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    """define the admin pages for user"""
    ordering = ['id']
    list_display = ['email','name','created_at']

admin.site.register(User,UserAdmin)