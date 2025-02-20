from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class IsDoctor(BasePermission):
    """
    Custom permission to allow only doctors to access certain views.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'doctor':
            return True
        raise PermissionDenied("Only doctors can access this resource.")


class IsAdmin(BasePermission):
    """
    Custom permission to allow only admins to access certain views.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'admin':
            return True
        raise PermissionDenied("Only admins can access this resource.")


class IsNurse(BasePermission):
    """
    Custom permission to allow only nurses to access certain views.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'nurse':
            return True
        raise PermissionDenied("Only nurses can access this resource.")


class IsPatient(BasePermission):
    """
    Custom permission to allow only patients to access certain views.
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'patient':
            return True
        raise PermissionDenied("Only patients can access this resource.")
