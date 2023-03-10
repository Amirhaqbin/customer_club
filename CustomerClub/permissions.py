import re
from rest_framework.permissions import BasePermission, SAFE_METHODS



class IsSuperUserOrIs_staff(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and request.user.is_superuser or 
            request.user and request.user.is_staff
        )


class ProfilePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            request.user and  
            request.user==obj.customer or 
            request.user.is_superuser or 
            request.user.is_staff

        )