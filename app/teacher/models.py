from django.db import models

from app.users.models import CustomUser

class Teacher(models.Model):

    user = models.OneToOneField(
    CustomUser,
    on_delete=models.CASCADE,
    related_name="teacher_profile",
    db_index=True
)

    full_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=150)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.full_name