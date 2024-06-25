from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow only admin users.
        return request.user and request.user.is_staff
