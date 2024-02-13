from django.db import models
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from product.models import Product
# Create your models here.

User = get_user_model()

class Favorite(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='favorites',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        User,
        related_name='favorites',
        on_delete=models.CASCADE
    )