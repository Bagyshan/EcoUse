from django.db import models
from category.models import Category
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()

class Product(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='products'
    )    
    title = models.CharField(max_length=150)
    body = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='products',
        null=True
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now = True)
    image = models.ImageField(upload_to='product_img/',null=True, blank=True)
    price = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now().date()
        super(Product, self).save(*args, **kwargs)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'