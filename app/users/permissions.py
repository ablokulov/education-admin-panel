from rest_framework.permissions import BasePermission


class Is_Admin(BasePermission):
    """
    Faqat role=ADMIN bo‘lgan foydalanuvchilarga ruxsat beradi
    """

    message = "Siz administrator emassiz"

    def has_permission(self, request, view):
        user = getattr(request, "user", None)

        # Schema + anonymous safety
        if not user or not user.is_authenticated:
            return False

        # CustomUser.is_admin_role property'ga mos
        return user.is_admin_role
