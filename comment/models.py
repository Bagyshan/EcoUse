from django.db import models
from django.db import models
from django.contrib.auth import get_user_model

from product.models import Product

# Create your models here.

User = get_user_model()
class Comment(models.Model):
    owner = models.ForeignKey(User, 
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
        related_name='comments'
    )

    def str(self):
        return f"Comment by {self.owner.username} on {self.title}"