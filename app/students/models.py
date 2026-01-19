from django.db import models

# Create your models here.


class Students(models.Model):
    
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)