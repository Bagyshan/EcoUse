from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
import openai
from chatbot import Chatbot

from category.models import Category
from home.models import House, Apartment
from home.views import HouseViewSet, ApartmentViewSet
from .models import HouseRecommendaion, ApartmentRecommendation
from .serializers import HouseRecommendationSerializer, ApartmentRecommendationSerializer
from product.models import Product
from product.serializers import ProductSerializer
from home.models import WindowEfficiency, WallInsulationEfficiency, RoofInsulationEfficiency, FloorInsulationEfficiency, HouseHeatingMethodEfficiency, ApartmentHeatingMethodEfficiency



# Create your views here.
User = get_user_model()

class HouseRecommendationViewSet(viewsets.ModelViewSet):
    queryset = HouseRecommendaion.objects.all()
    serializer_class = HouseRecommendationSerializer
    permission_classes = [IsAuthenticated]



    # @action(detail=True, methods=['get', 'post', 'patch', 'delete'])
    def get_house_recommendation(self, request, pk):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({'error': 'Please provide user_id'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        house = get_object_or_404(House, pk=pk)
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

        # def ask_gpt(higher:str, lower:str) -> str:
        #     response = g4f.ChatCompletion.create(
        #         model=g4f.models.gpt_4,
        #         messages=[{'role':'user', 'content':f'Чем хороши {higher}, и чем они лучше {lower}'}]
        #     )
        #     return response

        # window_category_list = []
        # for i in recommendation_dict['window_products']:
        #     window_category = Category.objects.get(id=i['category']).window_efficiency
        #     category_efficiency = window_category.insulation_efficiency
        #     if not category_efficiency in window_category_list:
        #         window_category_list.append(window_category)
        # window_recommendation_model = self.get_object()
        # window_title = 'Теплоэффективность окон'
        # window_category_dict = {}
        # for j in window_category_list:
        #     high = Category.objects.get(window_efficiency=j)
        #     low = house_window.name
        #     text = f'чем хороши {high.name}, и чем он лучше {low}'
        #     window_recommendation = window_recommendation_model.objects.create(
        #         title=window_title,
        #         description=Chatbot.ask_question(text),
        #         products=[x for x in recommendation_dict['window_products'] if x['category'] == high.id]
        #     )
        #     window_recommendation_serializer = HouseRecommendationSerializer(window_recommendation, many=True)
        #     window_category_dict[high.name] = window_recommendation_serializer.data

        

        return Response(recommendation_dict)


class ApartmentRecommendationViewSet(viewsets.ModelViewSet):
    queryset = ApartmentRecommendation.objects.all()
    serializer_class = ApartmentRecommendationSerializer
    permission_classes = [IsAuthenticated]


    # @action(detail=True, methods=['get', 'post', 'patch', 'delete'])
    def get_apartment_recommendation(self, request, pk):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({'error': 'Please provide user_id'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        apartment = get_object_or_404(Apartment, pk=pk)
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