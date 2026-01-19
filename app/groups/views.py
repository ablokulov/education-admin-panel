from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from app.users.permissions import Is_Admin
from .serializers import GroupsListSerializer
from .models import Group



class GroupsListCreateView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupsListSerializer
    permission_classes = [Is_Admin,IsAuthenticated]
    
class GroupsUpdateDistroyView(RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupsListSerializer
    permission_classes = [Is_Admin,IsAuthenticated]
    
    lookup_field = 'id'
    
  