from rest_framework import serializers
from .models import Group


class GroupsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"