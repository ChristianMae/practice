from django.urls import path
from .views import StorageCreateApiView, SendRequestViewSet

urlpatterns = [
    path('create/', StorageCreateApiView.as_view(), name="storage"),
    path('send-request/', SendRequestViewSet.as_view({'post':'post'}), name="send_request")
]
