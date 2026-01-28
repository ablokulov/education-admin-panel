from django.db import models
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from app.teacher.models import Teacher


class Group(models.Model):
    group_name = models.CharField(max_length=50, unique=True)

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.PROTECT,
        related_name="groups"
    )

    is_active = models.BooleanField(default=False, db_index=True)
    activated_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def activate(self):
        if self.is_active:
            return

        now = timezone.now()
        self.is_active = True
        self.activated_at = now
        self.expires_at = now + relativedelta(months=1)
        self.save()

    def deactivate(self):
        self.is_active = False
        self.expires_at = None
        self.save(update_fields=["is_active", "expires_at"])

    def __str__(self):
        return self.group_name
