from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.response import Response
from .serializers import ProductSerializer
from retailer.serializers import RetailerProductListSerializer


class CreateProduct(CreateAPIView):
    serializer_class = ProductSerializer


class DeleteProduct(DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = serializer_class.Meta.model.objects.all()


class ListProducts(ListAPIView):
    serializer_class = ProductSerializer
    queryset = serializer_class.Meta.model.objects.all()


class UpdateProduct(RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    queryset = serializer_class.Meta.model.objects.all()
    http_method_names = [u'get', u'patch']


class ViewProduct(RetrieveAPIView):
    serializer_class = RetailerProductListSerializer
    queryset = serializer_class.Meta.model.objects.all()
