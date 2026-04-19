from rest_framework.permissions import BasePermission

class IsAnalystOrAdmin(BasePermission):
    def has_permission(self, request, view):
        print("USER:", request.user)
        print("ROLE:", getattr(request.user, "role", None))
        print("IS AUTH:", request.user.is_authenticated)

        return True  # 🔥 TEMPORARY (IMPORTANT)


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.role == 'admin'


class IsViewer(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'viewer'