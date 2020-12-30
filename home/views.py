from django.shortcuts import render
from product.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    for product in products:
        print(product.Picture)
    return render(request, 'home/index.html', context)