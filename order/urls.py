from django.urls import path
from .views import displayOrders

urlpatterns = [
    path('display-orders', displayOrders, name='displayOrders')
]