from rest_framework import serializers
from .models import Students
from app.groups.serializers import GroupsListSerializer

class StudentDetailSerializer(serializers.ModelSerializer):
    group = GroupsListSerializer(read_only=True)
    
    class Meta:
        model = Students
        fields = [
            'id',
            'full_name',
            'phone',
            'created_at',
            'update_at',
            'group',  
        ]
        
        
class StudentlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'
