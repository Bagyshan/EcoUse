from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
# router.register('', WindowEfficiencyViewSet, basename='window')
router.register(r'window_efficiency', WindowEfficiencyViewSet)
router.register(r'house', HouseViewSet)
router.register(r'wall_insulation_efficiency', WallInsulationEfficiencyViewSet)
router.register(r'roof_insulation_efficiency', RoofInsulationEfficiencyViewSet)
router.register(r'floor_insulation_efficiency', FloorInsulationEfficiencyViewSet)
router.register(r'house_heating_method_efficiency', HouseHeatingMethodEfficiencyViewSet)
router.register(r'apartment_heating_method_efficiency', ApartmentHeatingMethodEfficiencyViewSet)
router.register(r'apartment', ApartmentViewSet)

urlpatterns = [
    path('', include(router.urls))
]