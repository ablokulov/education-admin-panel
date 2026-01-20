from django.db import models
from app.groups.models import Group


class Students(models.Model):
    
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=25,unique=True)
    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name='students')
    
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.full_name
    
    