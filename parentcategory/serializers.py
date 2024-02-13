from rest_framework.serializers import ModelSerializer

from .models import ParentCategory


class ParentCategorySerializer(ModelSerializer):
    class Meta:
        model = ParentCategory
        fields = '__all__'