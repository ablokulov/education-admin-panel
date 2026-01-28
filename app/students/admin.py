from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "full_name",
        "user",
        "group",
        "phone",
        "created_at",
    )

    list_filter = (
        "group",
        "created_at",
    )

    search_fields = (
        "full_name",
        "phone",
        "user__username",
        "user__email",
        "group__group_name",
    )

    ordering = ("-created_at",)

    readonly_fields = (
        "created_at",
        "updated_at",
    )
