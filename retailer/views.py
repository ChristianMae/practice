from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.response import Response
from .serializers import (
    RetailerSerializer, 
)


class CreateRetailer(CreateAPIView):
    """ Create retailer view class. """
    serializer_class = RetailerSerializer


class DeleteRetailer(DestroyAPIView):
    """ Delete retailer view class. """
    serializer_class = RetailerSerializer
    queryset = serializer_class.Meta.model.objects.all()


class ListRetailer(ListAPIView):
    """ List retailer view class. """
    serializer_class = RetailerSerializer
    queryset = serializer_class.Meta.model.objects.all()


class UpdateRetailer(RetrieveUpdateAPIView):
    """ Update retailer view class. """
    serializer_class = RetailerSerializer
    queryset = serializer_class.Meta.model.objects.all()
    http_method_names = [u'get', u'patch']


class ViewRetailer(RetrieveAPIView):
    serializer_class = RetailerSerializer
    queryset = serializer_class.Meta.model.objects.all()
