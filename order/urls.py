from django.urls import path
from .views import displayOrders, changeOrderConfirmation, confirmOrder

urlpatterns = [
    path('display-orders/', displayOrders, name='displayOrders'),
    path('change-order-confirmation/<int:id>', changeOrderConfirmation, name='changeOrderConfirmation'),
    path('confirmOrder/', confirmOrder, name='confirmOrder')
]