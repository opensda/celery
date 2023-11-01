from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator(BasePermission):
    message = "Для выполнения данного действия требуются права модератора"

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False


class IsOwner(BasePermission):
    message = "Для выполнения данного действия требуются права владельца объекта"

    def has_object_permission(self, request, view, obj):
        if request.user.role == obj.user:
            return True
        return False



