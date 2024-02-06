from rest_framework.permissions import BasePermission
from rest_framework import permissions

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class IsSeller(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.status == 'Seller'