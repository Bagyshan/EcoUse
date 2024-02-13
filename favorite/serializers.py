from rest_framework import serializers

from .models import Favorite


class FavoriteSerializer(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    product = serializers.ReadOnlyField(source='product.title')

    class Meta:
        fields = '__all__'
        model = Favorite
    
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        return repr['product']