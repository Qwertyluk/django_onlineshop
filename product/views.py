from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

# Create your views here.
def productDetails(request, id):
    """
    Displays a details page of the product with the specified id.

    **Context**

    ``product``
        Concrete product

    **Template:**

    :template:`product/details.html`
    """
    product = get_object_or_404(Product, id = id)
    context = {'product': product}
    return render(request, 'product/details.html', context)