from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

# Create your views here.
def productDetails(request, id):
    product = get_object_or_404(Product, id = id)
    print(product.Name)
    context = {'product': product}
    return render(request, 'product/details.html', context)