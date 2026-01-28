from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Profile

# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser

#     fieldsets = UserAdmin.fieldsets + (
#         ("Role info", {"fields": ("role",)}),
#     )

#     add_fieldsets = UserAdmin.add_fieldsets + (
#         ("Role info", {"fields": ("role",)}),
#     )



@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = (
        "id",
        "username",
        "email",
        "role",
        "is_staff",
        "is_active",
        "date_joined",
        "last_login",
    )
    list_filter = ("role", "is_staff", "is_active", "date_joined")
    search_fields = ("username", "email")
    ordering = ("username",)

    fieldsets = UserAdmin.fieldsets + (
        ("Role info", {"fields": ("role",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username",
                "email",
                "password1",
                "password2",
                "role",
                "is_staff",
                "is_superuser",
            ),
        }),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone")
    search_fields = ("user__username", "user__email")
