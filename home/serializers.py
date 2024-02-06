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
    window = WindowEfficiencySerializer()
    wall_insulation = WallInsulationEfficiencySerializer()
    roof_insulation = RoofInsulationEfficiencySerializer()
    floor_insulation = FloorInsulationEfficiencySerializer()
    heating_method = HouseHeatingMethodEfficiencySerializer()

    class Meta:
        model = House
        fields = '__all__'

class ApartmentSerializer(serializers.ModelSerializer):
    window = WindowEfficiencySerializer()
    floor_insulation = FloorInsulationEfficiencySerializer()
    heating_method = ApartmentHeatingMethodEfficiencySerializer()

    class Meta:
        model = Apartment
        fields = '__all__'