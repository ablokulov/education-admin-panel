
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN =  "ADMIN","Admin"
        
    role = models.CharField(max_length=8,choices=Role.choices,default=Role.ADMIN)
        

   