from django.db import models
from app.groups.models import Group
from app.users.models import CustomUser



class Student(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )

    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="students"
    )

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=25, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

