from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Recommendation
from .serializers import RecommendationSerializer
from product.models import Product
from home.models import House, Apartment
from django.contrib.auth import get_user_model
from category.models import Category
from product.serializers import ProductSerializer



# Create your views here.
User = get_user_model()
class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

    @action(detail=True, methods=['get'])
    def get_house_recommendation(self, request, pk):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({'error': 'Please provide user_id'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        house_window_efficiency = request.query_params('window').insulation_efficiency
        user_home_sum = request.query_params.get('sum_price')

        window_recommendation = Product.objects.filter(price__lte=user_home_sum, insulation_efficiency__gt=house_window_efficiency)

        serializer = ProductSerializer(window_recommendation, many=True)
        return Response(serializer.data)
    
        # house_wall_insulation_efficiency = request.data.get('wall_insulation').insulation_efficiency
        # house_roof_insulation_efficiency = request.data.get('roof_insulation').insulation_efficiency
        # house_floor_insulation_efficiency = request.data.get('floor_insulation').insulation_efficiency
        # house_heating_method_efficiency = request.data.get('heating_method').insulation_efficiency

        # house_window_queryset = Category.objects.get('window_efficiensy').insulation_efficiency
        # house_wall_insulation_queryset = Category.objects.get('window_efficiensy').insulation_efficiency
        # house_roof_insulation_queryset = Category.objects.get('window_efficiensy').insulation_efficiency
        # house_floor_insulation_queryset = Category.objects.get('window_efficiensy').insulation_efficiency
        # house_heating_method_queryset = Category.objects.get('window_efficiensy').insulation_efficiency