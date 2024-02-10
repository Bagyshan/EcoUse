from rest_framework import serializers
from rest_framework import serializers

from .models import HouseRecommendaion, ApartmentRecommendation


class HouseRecommendationSerializer(serializers.Model):
    class Meta:
        model = HouseRecommendaion
        fields = '__all__'

class ApartmentRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentRecommendation
        fields = '__all__'


