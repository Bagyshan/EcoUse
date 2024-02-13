from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProductViewSet, ProductListByCategory, ProductSearchList

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('category/<int:category_id>/', ProductListByCategory.as_view(), name='product-list-by-category'),
    path('category/search/', ProductSearchList.as_view(), name='product-list-by-category-search'),
]
