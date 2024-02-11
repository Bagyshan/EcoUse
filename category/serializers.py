from sre_parse import CATEGORIES
from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
    # def to_representation(self, instance):
    #     repr = super().to_representation(instance)
    #     children = Category.objects.all()
    #     if children:
    #         repr['categories'] = CategorySerializer(
    #             children, many=True
    #         ).data
    #     return repr
