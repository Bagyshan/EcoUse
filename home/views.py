from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from .models import *
from .serializers import * 
from product.serializers import ProductSerializer
from product.models import Product


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
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def post(self, request):
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    


class ApartmentViewSet(ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


