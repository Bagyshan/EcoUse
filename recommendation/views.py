from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

from home.views import HouseViewSet, ApartmentViewSet
from .models import HouseRecommendaion, ApartmentRecommendation
from .serializers import HouseRecommendationSerializer, ApartmentRecommendationSerializer



# Create your views here.
User = get_user_model()
class HouseRecommendationViewSet(viewsets.ModelViewSet):
    queryset = HouseRecommendaion.objects.all()
    serializer_class = HouseRecommendationSerializer

    



class ApartmentRecommendationViewSet(viewsets.ModelViewSet):
    queryset = ApartmentRecommendation.objects.all()
    serializer_class = ApartmentRecommendationSerializer
