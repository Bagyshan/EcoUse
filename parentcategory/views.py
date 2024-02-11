from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import ParentCategory
from .serializers import ParentCategorySerializer
from category.serializers import CategorySerializer

# Create your views here.
class ParentCategoryViewSet(ModelViewSet):
    queryset = ParentCategory.objects.all()
    serializer_class = ParentCategorySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]
        

    # @action(detail=True, methods=['get'])
    def get_child_categories(self, request, pk):
        parent_category = self.get_object()  # Получаем объект категории по её id
        categories = parent_category.children.all()  # Получаем все продукты для данной категории
        serializer = CategorySerializer(categories, many=True)  # Сериализуем данные о продуктах
        return Response(serializer.data) 