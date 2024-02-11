from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsOwner, IsSeller
from home.models import *
from rest_framework import generics
from rest_framework import filters

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
    
    
class ProductListByCategory(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.select_related('category').filter(category=category_id)
    

class ProductSearchList(generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        return Product.objects.all()
