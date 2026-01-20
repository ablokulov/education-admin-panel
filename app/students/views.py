
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import StudentlistSerializer,StudentDetailSerializer
from .models import Students
from app.users.permissions import Is_Admin

class StudentLisCreateView(ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentlistSerializer
    permission_classes = [Is_Admin,IsAuthenticated]


class StudentRetrievUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentDetailSerializer
    permission_classes = [Is_Admin,IsAuthenticated]
    
    lookup_field = 'id'