from django.db import models

# Create your models here.
class ParentCategory(models.Model):
    name = models.CharField(max_length=100)