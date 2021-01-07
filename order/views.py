from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order

# Create your views here.
@login_required(login_url='login')
def displayOrders(request):
    if request.user.is_staff:
        orders = Order.objects.all()
        context = {'orders': orders}
        return render(request, 'order/orders.html', context)
    else:
        messages.add_message(request, messages.ERROR , 'Insufficient authorization')
        return redirect('index')

@login_required(login_url='login')
def changeOrderConfirmation(request, id):
    if request.user.is_staff:
        order = get_object_or_404(Order, id = id)
        order.isConfirmed = not order.isConfirmed
        order.save()
        return redirect('displayOrders')
    else:
        messages.add_message(request, messages.ERROR , 'Insufficient authorization')
        return redirect('index')