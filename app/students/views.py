from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import StudentlistSerializer, StudentDetailSerializer
from .models import Student
from app.users.permissions import Is_Admin


class StudentListCreateView(ListCreateAPIView):
    serializer_class = StudentlistSerializer
    permission_classes = [IsAuthenticated, Is_Admin]

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Student.objects.none()
        return Student.objects.all()


class StudentRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentDetailSerializer
    permission_classes = [IsAuthenticated, Is_Admin]
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Student.objects.none()
        return Student.objects.all()
