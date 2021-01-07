from django.shortcuts import render
from .models import Order

# Create your views here.
def displayOrders(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'order/orders.html', context)