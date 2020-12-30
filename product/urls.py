from django.urls import path
from .views import productDetails

urlpatterns = [
    path('product-details/<int:id>', productDetails, name='productDetails'),
]