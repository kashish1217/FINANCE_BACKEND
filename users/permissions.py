from rest_framework.permissions import BasePermission

class IsAnalystOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.role in ['analyst', 'admin']


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.role == 'admin'


class IsViewer(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'viewer'