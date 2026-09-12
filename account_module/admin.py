from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.

@admin.register(CustomUser)
class CustomUser(UserAdmin):
    fieldsets = (
            (None, {"fields": ("username", "password")}),
            (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
            (
                _("Permissions"),
                {
                    "fields": (
                        "is_active",
                        "is_staff",
                        "is_superuser",
                        "groups",
                        "user_permissions",
                    ),
                },
            ),
            (_("Important dates"), {"fields": ("last_login", "date_joined")}),
            ('اطلاعات کاربر', {"fields": ("avatar", "about_author",'email_active_code','address')})
        )




