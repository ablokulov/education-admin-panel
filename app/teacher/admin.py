from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "full_name",
        "user",
        "profession",
        "created_at",
    )

    list_filter = (
        "profession",
        "created_at",
    )

    search_fields = (
        "full_name",
        "profession",
        "user__username",
        "user__email",
    )

    ordering = ("-created_at",)

    readonly_fields = (
        "created_at",
        "updated_at",
    )
