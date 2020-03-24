from django.urls import path 
from .views import (
    CreateRetailer,
    DeleteRetailer,
    ListRetailer,
    UpdateRetailer,
    ViewRetailer
)

urlpatterns = [
    path('retailers/', ListRetailer.as_view()),
    path('retailer/create/', CreateRetailer.as_view()),
    path('retailer/<int:pk>/', ViewRetailer.as_view()),
    path('retailer/<int:pk>/edit/', UpdateRetailer.as_view()),
    path('retailer/<int:pk>/delete/', DeleteRetailer.as_view())
]