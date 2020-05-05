from rest_framework import serializers
from product.serializers import ProductSerializer
from .models import Storage


class StorageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Storage
        fields = '__all__'


class SendRequestSerializer(serializers.Serializer):
    url = serializers.CharField()
