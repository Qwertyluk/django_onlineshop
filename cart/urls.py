from django.urls import path
from .views import addToCart, viewCart, removeFromCart, updateCartItemQuantity

urlpatterns = [
    path('addToCart/<int:id>-<int:quantity>/', addToCart, name='addToCart'),
    path('', viewCart, name='viewCart'),
    path('removeFromCart/<int:id>/', removeFromCart, name='removeFromCart'),
    path('updateCart/<int:id>-<int:quantity>/', updateCartItemQuantity, name='updateCartItemQuantity'),
]