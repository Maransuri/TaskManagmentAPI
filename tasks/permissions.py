from rest_framework import permissions

class IsAdminOrOwner(permissions.BasePermission):
    """
    Custom permission to allow only admins or task owners to modify tasks.
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user
