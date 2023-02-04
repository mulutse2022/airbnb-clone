from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):


    """Custom User Admin"""
    fieldsets = UserAdmin.fieldsets + (
        (
        "Custome Profile",
        {
        "fields": ("avatar", "gender", "bio", "birthdate", "language", "currency", "superhost")
        }
        
        ),
    )

    # list_display = ('username', "email", 'gender', 'language', 'currency', 'superhost')
    # list_filter = ('superhost', 'language', 'currency',)
