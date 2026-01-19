from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        USER = "USER", "User"
        ADMIN = "ADMIN", "Admin"

    role = models.CharField(
        max_length=5,
        choices=Role.choices,
        default=Role.USER
    )

    def __str__(self):
        return self.username

    @property
    def is_admin(self) -> bool:
        return self.role == self.Role.ADMIN
