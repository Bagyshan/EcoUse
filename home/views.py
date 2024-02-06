from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from .models import *
from .serializers import * 


class WindowEfficiencyViewSet(ModelViewSet):
    queryset = WindowEfficiency.objects.all()
    serializer_class = WindowEfficiencySerializer
    permission_classes = [IsAdminUser]

class WallInsulationEfficiencyViewSet(ModelViewSet):
    queryset = WallInsulationEfficiency.objects.all()
    serializer_class = WallInsulationEfficiencySerializer
    permission_classes = [IsAdminUser]

class RoofInsulationEfficiencyViewSet(ModelViewSet):
    queryset = RoofInsulationEfficiency.objects.all()
    serializer_class = RoofInsulationEfficiencySerializer
    permission_classes = [IsAdminUser]

class FloorInsulationEfficiencyViewSet(ModelViewSet):
    queryset = FloorInsulationEfficiency.objects.all()
    serializer_class = FloorInsulationEfficiencySerializer
    permission_classes = [IsAdminUser]

class HouseHeatingMethodEfficiencyViewSet(ModelViewSet):
    queryset = HouseHeatingMethodEfficiency.objects.all()
    serializer_class = HouseHeatingMethodEfficiencySerializer
    permission_classes = [IsAdminUser]

class ApartmentHeatingMethodEfficiencyViewSet(ModelViewSet):
    queryset = ApartmentHeatingMethodEfficiency.objects.all()
    serializer_class = ApartmentHeatingMethodEfficiencySerializer
    permission_classes = [IsAdminUser]

class HouseViewSet(ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    

class ApartmentViewSet(ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
