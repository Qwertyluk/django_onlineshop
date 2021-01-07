from django.db import models
from product.models import Product
from .infrastructure.modeldate import ModelDate

# Create your models here.
class DeliveryAddress(models.Model):
    firstName = models.CharField(max_length=150, blank=False)
    lastName = models.CharField(max_length=150, blank=False)
    email = models.EmailField(blank=False)

class Order(ModelDate):
    deliveryAddress = models.ForeignKey(DeliveryAddress, on_delete=models.DO_NOTHING)
    isConfirmed = models.BooleanField(default=False)

class OrderElement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)