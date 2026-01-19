from rest_framework.permissions import BasePermission


class Is_Admin(BasePermission):
    
    message = "Siz Adminstrator emassz"
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin
    