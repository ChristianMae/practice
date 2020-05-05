from django.urls import include, path
from .views import (
    CreateProduct,
    DeleteProduct,
    ListProducts,
    UpdateProduct,
    ViewProduct,
)

urlpatterns = [
    path('products/', ListProducts.as_view()),
    path('product/create/', CreateProduct.as_view()),
    path('retailer/<int:pk>/products/', ViewProduct.as_view()),
    path('product/<int:pk>/edit/', UpdateProduct.as_view()),
    path('product/<int:pk>/delete/', DeleteProduct.as_view()),
]