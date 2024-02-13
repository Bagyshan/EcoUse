from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParentCategoryViewSet

# Создаем маршрутизатор
router = DefaultRouter()
# Регистрируем представление в маршрутизаторе
router.register('', ParentCategoryViewSet)

# Определяем URL-маршруты
urlpatterns = [
    # Включаем маршруты из маршрутизатора
    path('', include(router.urls)),
    # Добавляем путь для действия get_child_categories
    path('<int:pk>/child-categories/', ParentCategoryViewSet.as_view({'get': 'get_child_categories'}), name='parent-category-child-categories'),
]