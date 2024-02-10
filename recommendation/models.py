from django.db import models

from home.models import House, Apartment


# Create your models here.
class HouseRecommendaion(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    products = models.ForeignKey(
        House,
        related_name='recommendations',
        on_delete=models.CASCADE
    )

class ApartmentRecommendation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    products = models.ForeignKey(
        Apartment,
        related_name='recommendations',
        on_delete=models.CASCADE
    )

