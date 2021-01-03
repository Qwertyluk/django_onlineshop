from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import register
from product.models import Product

# Create your views here.
@login_required(login_url='login')
def addToCart(request, id, quantity):
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
    
    print(request.session['cartItems'])
    return redirect('viewCart')

@login_required(login_url='login')
def viewCart(request):
    if request.session.has_key('cartItems'):
        sessionCartItems = request.session['cartItems']
        cartItems = []
        for sessionItem in sessionCartItems:
            product = get_object_or_404(Product, id = sessionItem['id'])
            cartItem = {'product': product, 'quantity': sessionItem['quantity']}
            cartItems.append(cartItem)

        for item in cartItems:
            print(item['product'].Picture)
    else:
        cartItems = None
    context = {'cartItems': cartItems}
    return render(request, 'cart/cart.html', context)

def cleanSession(request):
    request.session.flush()
    return redirect('index')

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)