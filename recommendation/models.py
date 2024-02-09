from django.db import models
from django.contrib.auth import get_user_model

from product.models import Product

# Create your models here.
User = get_user_model()

class Recommendation(models.Model):
    user = models.ForeignKey(User, related_name='recommendations',on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='recommendations', on_delete=models.CASCADE)