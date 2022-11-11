from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django import forms
# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    bio = forms.CharField(widget=forms.Textarea, required=False)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'bio')
        }),
    )
