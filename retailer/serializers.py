from rest_framework import serializers
from product.serializers import ProductSerializer
from .models import Retailer


class RetailerSerializer(serializers.ModelSerializer):
    """ Retailer model class. """

    class Meta:
        model = Retailer
        fields = [
            'name',
            'url'
        ]


class RetailerProductListSerializer(serializers.ModelSerializer):

    products = serializers.SerializerMethodField()

    class Meta:
        model = Retailer
        fields = [
            'name',
            'products',
        ]
    
    def get_products(self, obj):
        products = obj.product_set.prefetch_related()
        return ProductSerializer(products, many=True).data
