from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecommendationViewSet

router = DefaultRouter()
router.register(r'interactions', RecommendationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]