from rest_framework import serializers
from .models import Group
from app.teacher.serializers import TeacherListSerializer




class GroupsDetailSerializer(serializers.ModelSerializer):
    teacher = TeacherListSerializer(read_only=True)
    class Meta:
        model = Group
        fields = [
            'id', 
            'group_name',
            'created_at',
            'updated_at',
            'teacher',
        ]
        
        
class GroupsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"