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
    window_efficiency = models.ForeignKey(WindowEfficiency, on_delete=models.CASCADE, related_name='categories', blank=True, null=True)
    wall_insulation_efficiency = models.ForeignKey(WallInsulationEfficiency, on_delete=models.CASCADE, related_name='categories', blank=True, null=True)
    roof_insulation_efficiency = models.ForeignKey(RoofInsulationEfficiency, on_delete=models.CASCADE, related_name='categories', blank=True, null=True)
    floor_insulation_efficiency = models.ForeignKey(FloorInsulationEfficiency, on_delete=models.CASCADE, related_name='categories', blank=True, null=True)
    apartment_heating_method_efficiency = models.ForeignKey(ApartmentHeatingMethodEfficiency, on_delete=models.CASCADE, related_name='categories', blank=True, null=True)
    house_heating_method_efficiency = models.ForeignKey(HouseHeatingMethodEfficiency, on_delete=models.CASCADE, related_name='categories', blank=True, null=True)

    def __str__(self):
        # Проверяем, какое поле имеет значение и возвращаем его имя
        if self.window_efficiency:
            return self.window_efficiency.name
        elif self.wall_insulation_efficiency:
            return self.wall_insulation_efficiency.name
        elif self.roof_insulation_efficiency:
            return self.roof_insulation_efficiency.name
        elif self.floor_insulation_efficiency:
            return self.floor_insulation_efficiency.name
        elif self.apartment_heating_method_efficiency:
            return self.apartment_heating_method_efficiency.name
        elif self.house_heating_method_efficiency:
            return self.house_heating_method_efficiency.name
        else:
            return "No category selected" 
    # parent_category = models.ForeignKey(
    #     'self',
    #     on_delete=models.CASCADE,
    #     related_name='subcategories',
    #     null=True,
    #     blank=True
    # )
    
    # name = models.CharField(max_length=100)