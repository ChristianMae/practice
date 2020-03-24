from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """ Product serializer class"""

    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'active',
            'retailer'
        ]
