from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db import transaction

from app.groups.models import Group
from app.notifications.models import Notification
from app.students.models import Student


class Command(BaseCommand):
    help = "Muddati tugagan grouplarni no_active qiladi va notification yuboradi"

    def handle(self, *args, **kwargs):
        now = timezone.now()

        expired_groups = Group.objects.filter(
            is_active=True,
            expires_at__lte=now
        ).select_related("teacher", "teacher__user")

        count = 0

        for group in expired_groups:
            with transaction.atomic():
                group.deactivate()
                count += 1

                # 🔔 Teacher notification
                if group.teacher:
                    Notification.objects.create(
                        user=group.teacher.user,
                        title="Guruh muddati tugadi",
                        message=f"{group.group_name} guruhi no_active bo‘ldi"
                    )

                # 🔔 Student notifications (bulk)
                students = Student.objects.filter(
                    group=group
                ).select_related("user")

                Notification.objects.bulk_create([
                    Notification(
                        user=student.user,
                        title="Guruh no_active",
                        message="Sizning guruhingiz muddati tugadi"
                    )
                    for student in students
                ])

        self.stdout.write(
            self.style.SUCCESS(f"{count} ta group no_active qilindi")
        )
