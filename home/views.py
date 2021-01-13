from django.shortcuts import render
from product.models import Product, FILTER_CHOICES
from product.forms import FilterForm
from order.models import Order

# Create your views here.
def index(request):
    """
    Home page - displays all products and filter form.

    **Context**

    ``products``
        All products in the system.

    ``form``
        Instance of the filtering form.

    **Template:**

    :template:`home/index.html`
    """
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            isOnSale = form.cleaned_data.get('isOnSale')
            isAvailable = form.cleaned_data.get('isAvailable')
            filterChoice = form.cleaned_data.get('filterChoice')
            products = Product.objects.order_by(filterChoice)
            if isOnSale:
                products = products.filter(IsOnSale=isOnSale)
            if isAvailable:
                products = products.filter(IsAvailable=isAvailable)
            context = {'products': products, 'form': form}
            return render(request, 'home/index.html', context)
    
    products = Product.objects.all()
    form = FilterForm()
    context = {'products': products, 'form': form}
    return render(request, 'home/index.html', context)