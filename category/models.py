from django.db import models
from home.models import *


# class Category(models.Model):
#     NAME_CHOICE = (
#         (WindowEfficiency.__name__ + 'Category', 'Окна'),
#         (WallInsulationEfficiency.__name__ + 'Category', 'Стены'),
#         (RoofInsulationEfficiency.__name__ + 'Category', 'Крыша'),
#         (FloorInsulationEfficiency.__name__ + 'Category', 'Полы'),
#         (HouseHeatingMethodEfficiency.__name__ + 'Category', 'Методы отопления домов'),
#         (ApartmentHeatingMethodEfficiency.__name__ + 'Category', 'Методы отопления квартир')
#     )

#     name = models.CharField(choices=NAME_CHOICE, unique=True)

#     def __str__(self) -> str:
#         return self.name
    
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'



class Category(models.Model):
    parent_category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='subcategories',
        null=True,
        blank=True
    )
    
    name = models.CharField(max_length=100)
    window_efficiency = models.ForeignKey(WindowEfficiency, on_delete=models.CASCADE, related_name='categories', blank=True, null=True)
    wall_insulation_efficiency = models.ForeignKey(WallInsulationEfficiency, on_delete=models.CASCADE, related_name='categories', blank=True, null=True)
    roof_insulation_efficiency = models.ForeignKey(RoofInsulationEfficiency, on_delete=models.CASCADE, related_name='categories', blank=True, null=True)
    floor_insulation_efficiency = models.ForeignKey(FloorInsulationEfficiency, on_delete=models.CASCADE, related_name='categories', blank=True, null=True)
    apartment_heating_method_efficiency = models.ForeignKey(ApartmentHeatingMethodEfficiency, on_delete=models.CASCADE, related_name='categories', blank=True, null=True)
    house_heating_method_efficiency = models.ForeignKey(HouseHeatingMethodEfficiency, on_delete=models.CASCADE, related_name='categories', blank=True, null=True)

    def __str__(self):
        return self.name