from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from home.models import *
from rest_framework import generics
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from .models import Product
from .serializers import ProductSerializer
from .permissions import IsOwner, IsSeller
from favorite.models import Favorite
from comment.serializers import CommentSerializer


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

    @swagger_auto_schema(method='POST', request_body=CommentSerializer, operation_description='add comment for post')
    @action(detail=True, methods=['POST'])
    def comment(self, request, pk=None):
        post = self.get_object()
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(post=post, owner=request.user)
        return Response('успешно добавлено', 201)
    
    @action(detail=True, methods=['POST'])
    def toggle_favorite(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        favorite = request.user.favorites.filter(product=product)
        
        if favorite.exists():
            favorite.delete()
            return Response('Удалено из избранных', status=204)
        
        Favorite.objects.create(product=product, owner=request.user)
        return Response('Добавлено в избранное', status=201)
    
    
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
