from django.shortcuts import get_object_or_404
from django.db import transaction

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.notifications.models import Notification
from app.students.models import Student
from app.users.permissions import Is_Admin


from drf_spectacular.utils import extend_schema

from .serializers import GroupsListSerializer,GroupsDetailSerializer
from .models import Group



class GroupsListCreateView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupsListSerializer
    permission_classes = [Is_Admin,IsAuthenticated]
    
class GroupsUpdateDistroyView(RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupsDetailSerializer
    permission_classes = [Is_Admin,IsAuthenticated]
    
    lookup_field = 'id'
    


class ActivateGroupView(APIView):
    permission_classes = [IsAuthenticated, Is_Admin]

    @extend_schema(
        request=None,
        responses={
            200: {
                "type": "object",
                "properties": {
                    "tokens": {
                        "type": "object",
                        "properties": {
                            "access": {"type": "string"},
                            "refresh": {"type": "string"},
                        }
                    }
                }
            }
        },
        auth=[]
    )
    def post(self, request):
        group_id = request.data.get("group_id")

        if not group_id:
            return Response(
                {"detail": "group_id talab qilinadi"},
                status=400
            )

        group = get_object_or_404(Group, id=group_id)

        with transaction.atomic():
            group.activate()

            if group.teacher:
                Notification.objects.create(
                    user=group.teacher.user,
                    title="Guruh aktivlashtirildi",
                    message=f"{group.group_name} guruhi 1 oyga aktiv qilindi"
                )

            students = Student.objects.filter(group=group).select_related("user")
            Notification.objects.bulk_create([
                Notification(
                    user=student.user,
                    title="Guruh aktiv",
                    message=f"Sizning {group.group_name} guruhingiz aktiv bo‘ldi"
                )
                for student in students
            ])

        return Response(
            {
                "detail": "Group aktiv qilindi",
                "expires_at": group.expires_at
            }
        )
