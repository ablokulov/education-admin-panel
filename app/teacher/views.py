from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from app.users.permissions import Is_Admin
from .models import Teacher
from .serializers import TeacherListSerializer


class ListCreateViews(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer
    permission_classes = [Is_Admin,IsAuthenticated]
    
class UpdateViews(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer
    permission_classes = [Is_Admin,IsAuthenticated]
    
    lookup_field = 'id'
    