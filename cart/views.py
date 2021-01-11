from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from product.models import Product
from order.models import DeliveryAddress, Order, OrderElement
from order.forms import DeliveryAddressForm

# Create your views here.
@login_required(login_url='login')
def addToCart(request, id, quantity):
    product = get_object_or_404(Product, id = id)
    if product.IsAvailable:
        if request.session.has_key('cartItems'):
            cartItems = request.session['cartItems']
            found = False
            for item in cartItems:
                if item['id'] == id:
                    found = True
                    item['quantity'] = item['quantity'] + quantity
            if found == False:
                cartItems.append({'id': id, 'quantity': quantity})
            request.session['cartItems'] = cartItems
        else:
            cartItems = [{'id': id, 'quantity': quantity}]
            request.session['cartItems'] = cartItems
    return redirect('viewCart')

@login_required(login_url='login')
def viewCart(request):
    if request.session.has_key('cartItems'):
        cartItems = []
        sessionCartItems = request.session['cartItems']
        if len(sessionCartItems) > 0:
            for sessionItem in sessionCartItems:
                product = get_object_or_404(Product, id = sessionItem['id'])
                cartItem = {'product': product, 'quantity': sessionItem['quantity']}
                cartItems.append(cartItem)
        else:
            cartItems = None
    else:
        cartItems = None

    deliveryCost = "{:.2f}".format(2)
    initial_dict = { 
        "firstName" : request.user.first_name, 
        "lastName" : request.user.last_name, 
        "email": request.user.email, 
    } 
    deliveryAddressForm = DeliveryAddressForm(initial = initial_dict)
    context = {'cartItems': cartItems, 'deliveryCost': deliveryCost, 'deliveryAddressForm': deliveryAddressForm}
    return render(request, 'cart/cart.html', context)

@login_required(login_url='login')
def removeFromCart(request, id):
    if request.session.has_key('cartItems'):
        cartItems = request.session['cartItems']
        index = 0
        for cartItem in cartItems:
            if cartItem['id'] == id:
                cartItems.pop(index)
                request.session['cartItems'] = cartItems
                break
            index = index + 1

    return redirect('viewCart')

@login_required(login_url='login')
def updateCartItemQuantity(request, id, quantity):
    if request.session.has_key('cartItems'):
        cartItems = request.session['cartItems']
        for cartItem in cartItems:
            if cartItem['id'] == id:
                cartItem['quantity'] = quantity
                request.session['cartItems'] = cartItems
                break
    return redirect('viewCart')

