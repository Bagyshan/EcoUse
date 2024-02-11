from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class WindowEfficiency(models.Model):
    window_view = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    insulation_efficiency = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class WallInsulationEfficiency(models.Model):
    wall_insulation_view = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    insulation_efficiency = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class RoofInsulationEfficiency(models.Model):
    roof_insulation_view = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    insulation_efficiency = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class FloorInsulationEfficiency(models.Model):
    floor_insulation_view = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    insulation_efficiency = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class HouseHeatingMethodEfficiency(models.Model):
    house_heating_method_view = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    insulation_efficiency = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class ApartmentHeatingMethodEfficiency(models.Model):
    apartment_heating_method_view = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    insulation_efficiency = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class House(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='houses',
        on_delete=models.CASCADE
    )
    area = models.PositiveIntegerField()
    window = models.ForeignKey(WindowEfficiency, related_name='houses', on_delete=models.CASCADE, null=True, blank=True)
    window_quantity = models.PositiveIntegerField()
    wall_insulation = models.ForeignKey(WallInsulationEfficiency, related_name='houses', on_delete=models.CASCADE, null=True, blank=True)
    roof_insulation = models.ForeignKey(RoofInsulationEfficiency, related_name='houses', on_delete=models.CASCADE, null=True, blank=True)
    floor_insulation  = models.ForeignKey(FloorInsulationEfficiency, related_name='houses', on_delete=models.CASCADE, null=True, blank=True)
    heating_method = models.ForeignKey(HouseHeatingMethodEfficiency, related_name='houses', on_delete=models.CASCADE, null=True, blank=True)
    sum_price = models.PositiveIntegerField()



class Apartment(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='apartments',
        on_delete=models.CASCADE
    )
    area = models.PositiveIntegerField()
    window = models.ForeignKey(WindowEfficiency, related_name='apartments', on_delete=models.CASCADE, null=True, blank=True)
    window_quantity = models.PositiveIntegerField()
    floor_insulation  = models.ForeignKey(FloorInsulationEfficiency, related_name='apartments', on_delete=models.CASCADE, null=True, blank=True)
    heating_method = models.ForeignKey(ApartmentHeatingMethodEfficiency, related_name='apartments', on_delete=models.CASCADE, null=True, blank=True)
    sum_price = models.PositiveIntegerField()   
