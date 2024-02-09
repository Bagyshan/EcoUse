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

        if not house_window:
            return Response({'error': 'House window is not specified'}, status=status.HTTP_400_BAD_REQUEST)

        house_window_efficiency = house_window.insulation_efficiency
        user_home_sum = house.sum_price

        products_by_price = Product.objects.filter(price__lte=user_home_sum)
        # filtered_products = products_by_price.filter(category__insulation_efficiency__gte=house_window_efficiency)
        filtered_products = products_by_price.filter(category__insulation_efficiency__gte=house_window.insulation_efficiency)

        # list1 = list(filter(lambda x: x['category'].insulation_efficiency >= house_window_efficiency, products_by_price))
        serializer = ProductSerializer(filtered_products, many=True)
        return Response(serializer.data)
        # house_window_category = house.categories

        # window_recommendation = products_by_price.filter(
        #     category__insulation_efficiency__gt=house_window_efficiency
        # )
        # house = self.get_object()
        # house_window_efficiency = house.window.insulation_efficiency
        # user_home_sum = house.sum_price

        # products_by_price = Product.objects.filter(price__lte=user_home_sum)
        # window_recommendation = products_by_price.filter(
        #     insulation_efficiency__gt=house_window_efficiency
        # )


        # # window_recommendation = Product.objects.filter(
        # #     price__lte=user_home_sum, 
        # #     category__window_id=house_window_efficiency,
        # #     insulation_efficiency__gt=house_window_efficiency
        # # )
        # # house_window_category = house.window.category
        # # window_recommendation = Product.objects.filter(
        # #     Q(category=house_window_category) & Q(category__insulation_efficiency__gt=house_window_efficiency),
        # #     price__lte=user_home_sum,
        # # )

        # serializer = ProductSerializer(window_recommendation, many=True)
        # return Response(serializer.data)
    

class ApartmentViewSet(ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
