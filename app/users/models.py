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
    def is_admin_role(self) -> bool:
        return self.role == self.Role.ADMIN


class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username