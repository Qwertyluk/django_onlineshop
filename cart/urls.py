from django.urls import path
from .views import addToCart, cleanSession, viewCart

urlpatterns = [
    path('addToCart/<int:id>-<int:quantity>/', addToCart, name='addToCart'),
    path('', viewCart, name='viewCart'),
    path('clean/', cleanSession, name='cleanSession')
]