from django.db import models
from home.models import *


class Category(models.Model):
    NAME_CHOICE = (
        (WindowEfficiency.__name__ + 'Category', 'Окна'),
        (WallInsulationEfficiency.__name__ + 'Category', 'Стены'),
        (RoofInsulationEfficiency.__name__ + 'Category', 'Крыша'),
        (FloorInsulationEfficiency.__name__ + 'Category', 'Полы'),
        (HouseHeatingMethodEfficiency.__name__ + 'Category', 'Методы отопления домов'),
        (ApartmentHeatingMethodEfficiency.__name__ + 'Category', 'Методы отопления квартир')
    )

    name = models.CharField(choices=NAME_CHOICE, unique=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'