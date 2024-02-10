from rest_framework.viewsets import ModelViewSet
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

    @action(detail=True, methods=['get'])
    def get_house_recommendation(self, request, pk):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({'error': 'Please provide user_id'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        house = self.get_object()
        house_window = house.window
        house_wall_insulation = house.wall_insulation
        house_roof_insulation = house.roof_insulation
        house_floor_insulation = house.floor_insulation
        house_heating_method = house.heating_method


        house_window_efficiency = house_window.insulation_efficiency
        house_wall_insulation_efficiency = house_wall_insulation.insulation_efficiency
        house_roof_insulation_efficiency = house_roof_insulation.insulation_efficiency
        house_floor_insulation_efficiency = house_floor_insulation.insulation_efficiency
        house_heating_method_efficiency = house_heating_method.insulation_efficiency

        user_home_sum = house.sum_price

        product_by_price = Product.objects.filter(price__lte=user_home_sum)

        all_window_categories = WindowEfficiency.objects.all()
        window_product = product_by_price.exclude(category__window_efficiency__insulation_efficiency__lt=house_window_efficiency).exclude(category__window_efficiency__insulation_efficiency=house_window_efficiency).filter(category__window_efficiency__in=all_window_categories)

        all_wall_insulation_categories = WallInsulationEfficiency.objects.all()
        wall_insulation_product = product_by_price.exclude(category__wall_insulation_efficiency__insulation_efficiency__lt=house_wall_insulation_efficiency).exclude(category__wall_insulation_efficiency__insulation_efficiency=house_wall_insulation_efficiency).filter(category__wall_insulation_efficiency__in=all_wall_insulation_categories)

        all_roof_insulation_categories = RoofInsulationEfficiency.objects.all()
        roof_insulation_product = product_by_price.exclude(category__roof_insulation_efficiency__insulation_efficiency__lt=house_roof_insulation_efficiency).exclude(category__roof_insulation_efficiency__insulation_efficiency=house_roof_insulation_efficiency).filter(category__roof_insulation_efficiency__in=all_roof_insulation_categories)

        all_floor_insulation_categories = FloorInsulationEfficiency.objects.all()
        floor_insulation_product = product_by_price.exclude(category__floor_insulation_efficiency__insulation_efficiency__lt=house_floor_insulation_efficiency).exclude(category__floor_insulation_efficiency__insulation_efficiency=house_floor_insulation_efficiency).filter(category__floor_insulation_efficiency__in=all_floor_insulation_categories)

        all_house_heating_method_categories = HouseHeatingMethodEfficiency.objects.all()
        house_heating_method_product = product_by_price.exclude(category__house_heating_method_efficiency__insulation_efficiency__lt=house_heating_method_efficiency).exclude(category__house_heating_method_efficiency__insulation_efficiency=house_heating_method_efficiency).filter(category__house_heating_method_efficiency__in=all_house_heating_method_categories)


        window_serializer = ProductSerializer(window_product, many=True)
        wall_insulation_serializer = ProductSerializer(wall_insulation_product, many=True)
        roof_insulation_serializer = ProductSerializer(roof_insulation_product, many=True)
        floor_insulation_serializer = ProductSerializer(floor_insulation_product, many=True)
        house_heating_method_serializer = ProductSerializer(house_heating_method_product, many=True)
        recommendation_dict = {
            'window_products': window_serializer.data,
            'wall_insulation_products': wall_insulation_serializer.data,
            'roof_insulation_products': roof_insulation_serializer.data,
            'floor_insulation_products': floor_insulation_serializer.data,
            'house_heating_method_products': house_heating_method_serializer.data
        }
        return Response(recommendation_dict)
    


class ApartmentViewSet(ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['get'])
    def get_house_recommendation(self, request, pk):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({'error': 'Please provide user_id'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        apartment = self.get_object()
        apartment_window = apartment.window
        apartment_floor_insulation = apartment.floor_insulation
        apartment_heating_method = apartment.heating_method


        apartment_window_efficiency = apartment_window.insulation_efficiency
        apartment_floor_insulation_efficiency = apartment_floor_insulation.insulation_efficiency
        apartment_heating_method_efficiency = apartment_heating_method.insulation_efficiency

        user_home_sum = apartment.sum_price

        product_by_price = Product.objects.filter(price__lte=user_home_sum)

        all_window_categories = WindowEfficiency.objects.all()
        window_product = product_by_price.exclude(category__window_efficiency__insulation_efficiency__lt=apartment_window_efficiency).exclude(category__window_efficiency__insulation_efficiency=apartment_window_efficiency).filter(category__window_efficiency__in=all_window_categories)

        all_floor_insulation_categories = FloorInsulationEfficiency.objects.all()
        floor_insulation_product = product_by_price.exclude(category__floor_insulation_efficiency__insulation_efficiency__lt=apartment_floor_insulation_efficiency).exclude(category__floor_insulation_efficiency__insulation_efficiency=apartment_floor_insulation_efficiency).filter(category__floor_insulation_efficiency__in=all_floor_insulation_categories)

        all_apartment_heating_method_categories = ApartmentHeatingMethodEfficiency.objects.all()
        apartment_heating_method_product = product_by_price.exclude(category__apartment_heating_method_efficiency__insulation_efficiency__lt=apartment_heating_method_efficiency).exclude(category__apartment_heating_method_efficiency__insulation_efficiency=apartment_heating_method_efficiency).filter(category__apartment_heating_method_efficiency__in=all_apartment_heating_method_categories)


        window_serializer = ProductSerializer(window_product, many=True)
        floor_insulation_serializer = ProductSerializer(floor_insulation_product, many=True)
        apartment_heating_method_serializer = ProductSerializer(apartment_heating_method_product, many=True)
        recommendation_dict = {
            'window_products': window_serializer.data,
            'floor_insulation_products': floor_insulation_serializer.data,
            'house_heating_method_products': apartment_heating_method_serializer.data
        }
        return Response(recommendation_dict)
