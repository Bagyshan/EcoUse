from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsOwner, IsSeller
from django.db.models.signals import pre_save
from django.dispatch import receiver
from home.models import *

class StandartResultPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandartResultPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE','POST']:
            return [permissions.IsAuthenticated(), IsOwner(), IsSeller()]
        return [permissions.IsAuthenticatedOrReadOnly()]