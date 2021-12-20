from rest_framework import permissions

from apps.bars.models import Bar


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user:
            try:
                bar = Bar.objects.get(id=request.data.get("bar"))
            except Exception:
                return False
            return bar.owner == request.user or request.user.is_superuser


def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
        return True
    return getattr(obj, "created_by") == request.user or getattr(
        request.user, "is_superuser"
    )
