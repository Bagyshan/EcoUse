from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HouseRecommendationViewSet, ApartmentRecommendationViewSet

# router = DefaultRouter()
# router.register(r'house-recommendations', HouseRecommendationViewSet, basename='house-recommendations')
# router.register(r'apartment-recommendations', ApartmentRecommendationViewSet, basename='apartment-recommendations')

urlpatterns = [
    path('house-recommendations/<int:pk>/get-house-recommendation/', HouseRecommendationViewSet.as_view({'get': 'get_house_recommendation'}), name='get-house-recommendation'),
    path('apartment-recommendations/<int:pk>/get-apartment-recommendation/', ApartmentRecommendationViewSet.as_view({'get': 'get_apartment_recommendation'}), name='get-apartment-recommendation')
]   

# urlpatterns += router.urls