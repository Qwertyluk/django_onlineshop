from django.db import models

class Product(models.Model):
    Name = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=19, decimal_places=2)
    Description = models.CharField(max_length=10000)
    Picture = models.CharField(max_length=300)
