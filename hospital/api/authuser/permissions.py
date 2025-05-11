from rest_framework.permissions import BasePermission
from django.db.models import Q

class IsAdminUserGroup(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='admin').exists()

class IsAuthenticatedUserRole(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(
            Q(name='admin') | Q(name='doctor') | Q(name='paciente')
        ).exists()

    def has_object_permission(self, request, view, obj):
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return request.user.groups.filter(Q(name='admin') | Q(name='doctor')).exists()
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return request.user.groups.filter(Q(name='admin') | Q(name='doctor') | Q(name='paciente')).exists()
        return False
