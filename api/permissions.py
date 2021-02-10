from rest_framework import permissions

from users.models import CustomUser


class IsSuperUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_superuser
        )


class ReviewPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_anonymous:
            return False
        else:
            return (
                obj.author == request.user
                or request.user.role in (
                    CustomUser.Roles.ADMIN, CustomUser.Roles.MODERATOR
                )
            )


class CommentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            if request.method == 'GET':
                return True
        else:
            return (
                obj.author == request.user
                or request.user.role in (
                    CustomUser.Roles.ADMIN, CustomUser.Roles.MODERATOR
                )
            )
