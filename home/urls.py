from django.urls import path
from .views import index, displayOrders

urlpatterns = [
    path('', index, name='index'),
    path('orders', displayOrders, name='displayOrders')
]