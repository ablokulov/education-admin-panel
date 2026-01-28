from rest_framework import serializers
from .models import Student
from app.groups.serializers import GroupsListSerializer

class StudentDetailSerializer(serializers.ModelSerializer):
    group = GroupsListSerializer(read_only=True)
    
    class Meta:
        model = Student
        fields = [
            'id',
            'full_name',
            'phone',
            'created_at',
            'updated_at',
            'group',  
        ]
        
        
class StudentlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
