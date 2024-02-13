from django.db import models
from django.contrib.auth import get_user_model

from home.models import House, Apartment
from product.models import Product


class HouseRecommendaion(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # products = models.JSONField()

class ApartmentRecommendation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    products = models.JSONField()

