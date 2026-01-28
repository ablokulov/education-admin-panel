from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from app.users.permissions import Is_Admin
from .models import Teacher
from .serializers import TeacherListSerializer

class ListCreateViews(ListCreateAPIView):
    serializer_class = TeacherListSerializer
    permission_classes = [IsAuthenticated, Is_Admin]

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Teacher.objects.none()
        return Teacher.objects.all()


class UpdateViews(RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherListSerializer
    permission_classes = [IsAuthenticated, Is_Admin]
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Teacher.objects.none()
        return Teacher.objects.all()

    