from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import Order, DeliveryAddress, OrderElement
from .forms import DeliveryAddressForm
from product.models import Product

# Create your views here.
@login_required(login_url='login')
def displayOrders(request):
    """
    Displays each order confirmed by users.

    **Context**

    ``orders``
        All orders confirmed by users.

    **Template:**

    If user is staff then returns :template:`order/orders.html`.
    If user is not staff then redirets to the index endpoint.
    """
    if request.user.is_staff:
        orders = Order.objects.all()
        context = {'orders': orders}
        return render(request, 'order/orders.html', context)
    else:
        messages.add_message(request, messages.ERROR , 'Insufficient authorization')
        return redirect('index')

@login_required(login_url='login')
def changeOrderConfirmation(request, id):
    """
    Change the confirmation state of the order with the specified id.

    **Template:**

    If user is staff then redirects displayOrders endpoint.
    If user is not staff then redirets to the index endpoint.
    """
    if request.user.is_staff:
        order = get_object_or_404(Order, id = id)
        order.isConfirmed = not order.isConfirmed
        order.save()
        return redirect('displayOrders')
    else:
        messages.add_message(request, messages.ERROR , 'Insufficient authorization')
        return redirect('index')

@login_required(login_url='login')
def confirmOrder(request):
    """
    Confirms users orders.

    **Template:**

    If the confirmation is success then redirects to the index endpoint.
    If the confirmation is not succes then redirect to the cart endpoint.
    """
    if request.method == 'POST':
        if request.session.has_key('cartItems'):
            sessionCartItems = request.session['cartItems']
            if len(sessionCartItems) > 0:
                form = DeliveryAddressForm(request.POST)
                if form.is_valid():
                    firstName = form.cleaned_data['firstName']
                    lastName = form.cleaned_data['lastName']
                    email = form.cleaned_data['email']
                    deliveryAddress = DeliveryAddress(firstName = firstName, lastName = lastName, email = email)
                    deliveryAddress.save()
                    order = Order(deliveryAddress = deliveryAddress)
                    order.save()
                    orderPrice = 0
                    for cartItem in sessionCartItems:
                        product = get_object_or_404(Product, id = cartItem['id'])
                        orderPrice = orderPrice + (product.Price * cartItem['quantity'])
                        orderElement = OrderElement(product = product, quantity = cartItem['quantity'], order = order)
                        orderElement.save()
                    context={"firstName": firstName, "orderPrice": orderPrice, "orderId": order.id}
                    htmlContent = render_to_string("email.html", context)
                    textContent = strip_tags(htmlContent)
                    email = EmailMultiAlternatives(
                        "Order confirmation",
                        textContent,
                        settings.EMAIL_HOST_USER,
                        [email]
                    )
                    email.send()
                    messages.add_message(request, messages.SUCCESS, 'Order has been accepted')
                    del request.session['cartItems']
                    return redirect('index')
    
    return redirect('viewCart')