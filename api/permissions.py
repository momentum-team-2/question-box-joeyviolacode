from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Covers GET HEAD and OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        # Otherwise we need to know if user is owner
        return obj.author == request.user