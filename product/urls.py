from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProductViewSet, ProductListByCategory

router = DefaultRouter()
router.register('', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:category_id>/',ProductListByCategory.as_view(), name='product-list-by-category')
]