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

class IsRadiologist(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'radiologist':
            return True
        raise PermissionDenied("Only radiologists can access this resource.")

class IsLabTechnician(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'lab_technician':
            return True
        raise PermissionDenied("Only lab technicians can access this resource.")

class IsPharmacist(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'pharmacist':
            return True
        raise PermissionDenied("Only pharmacists can access this resource.")

class IsDataAnalyst(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'data_analyst':
            return True
        raise PermissionDenied("Only data analysts can access this resource.")

class IsPublicHealthOfficial(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'public_health_official':
            return True
        raise PermissionDenied("Only public health officials can access this resource.")
