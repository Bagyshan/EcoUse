from rest_framework.viewsets import ModelViewSet
from product.serializers import ProductSerializer
from .models import Category
from .serializers import CategorySerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]
    
    # @action(detail=True, methods=['get'])
    def get_category_products(self, request, pk):
        category = self.get_object()  # Получаем объект категории по её id
        products = category.products.all()  # Получаем все продукты для данной категории
        serializer = ProductSerializer(products, many=True)  # Сериализуем данные о продуктах
        return Response(serializer.data) 