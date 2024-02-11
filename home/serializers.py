from rest_framework import serializers
from .models import *


class WindowEfficiencySerializer(serializers.ModelSerializer):
    class Meta:
        model = WindowEfficiency
        fields = '__all__'

class WallInsulationEfficiencySerializer(serializers.ModelSerializer):
    class Meta:
        model = WallInsulationEfficiency
        fields = '__all__'

class RoofInsulationEfficiencySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoofInsulationEfficiency
        fields = '__all__'

class FloorInsulationEfficiencySerializer(serializers.ModelSerializer):
    class Meta:
        model = FloorInsulationEfficiency
        fields = '__all__'

class HouseHeatingMethodEfficiencySerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseHeatingMethodEfficiency
        fields = '__all__'

class ApartmentHeatingMethodEfficiencySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentHeatingMethodEfficiency
        fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    # window = WindowEfficiencySerializer(required=False)
    # wall_insulation = WallInsulationEfficiencySerializer(required=False)
    # roof_insulation = RoofInsulationEfficiencySerializer(required=False)
    # floor_insulation = FloorInsulationEfficiencySerializer(required=False)
    # heating_method = HouseHeatingMethodEfficiencySerializer(required=False)

    class Meta:
        model = House
        fields = '__all__'

class ApartmentSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    # window = WindowEfficiencySerializer(required=False)
    # floor_insulation = FloorInsulationEfficiencySerializer(required=False)
    # heating_method = ApartmentHeatingMethodEfficiencySerializer(required=False)

    class Meta:
        model = Apartment
        fields = '__all__'