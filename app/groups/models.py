from django.db import models
from app.teacher.models import Teacher


class Group(models.Model):
    
    group_name = models.CharField(max_length=50,unique=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.DO_NOTHING,related_name="group")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.group_name