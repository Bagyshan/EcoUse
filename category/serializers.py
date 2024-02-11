from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
    # def to_representation(self, instance):
    #     repr = super().to_representation(instance)
    #     products = instance.products.all()
    #     if products:
    #         repr['children'] = CategorySerializer(
    #             products, many=True
    #         ).data
    #     return repr