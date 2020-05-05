import requests
from django.shortcuts        import render
from rest_framework          import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers            import StorageSerializer, SendRequestSerializer


class StorageCreateApiView(CreateAPIView):
    serializer_class = StorageSerializer


class SendRequestViewSet(ViewSet):
    serializer_class = SendRequestSerializer

    def post(self, request, *args, **kwargs):
        url = request.data['url']
        if not url:
            url = 'http://localhost:8000/create/'
        
        payload = {
            'url': url,
            'data': str(request.META)
        }
        resp = requests.post(url, data=payload)
        return Response(resp.status_code, status=status.HTTP_201_CREATED)
