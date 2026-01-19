from django.db import models

# Create your models here.


class Teacher(models.Model):
    
    full_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=150)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.full_name