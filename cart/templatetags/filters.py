from django.template.defaultfilters import register
from django import template
from decimal import *

@register.filter
def fromDictGetItemAttribute(dictionary, itemAttribute):
    """
    Returns the attribute of a dictionary element. The element and attribute name are provided as the second parameter and are separeted by a comma.
    """
    itemAttribute = itemAttribute.split(',')
    item = dictionary.get(itemAttribute[0])
    if hasattr(item, itemAttribute[1]):
        return getattr(item, itemAttribute[1])
    else:
        return None

@register.filter
def fromDictGetItemValue(dictionary, itemName):
    """
    Returns an item from the dictionary.
    """
    return dictionary.get(itemName)

@register.filter
def calculateCartItemValue(dictionary):
    """
    Returns the cart element value. 
    """
    product = dictionary.get('product')
    quantity = dictionary.get('quantity')
    return product.Price * quantity

@register.filter
def getProductNum(list):
    """
    Returns the quantity of products in the list.
    """
    quantity = 0
    for item in list:
        quantity = quantity + item.get('quantity')
    return quantity

@register.filter
def calculateCartValue(list):
    """
    Calculates the total price of the order's elements.
    """
    value = 0
    for item in list:
        product = item.get('product')
        value = value + (product.Price * item.get('quantity'))
    return value

@register.filter
def calculateCartFinalValue(list, deliveryCost):
    """
    Calculates the total price of the order. 
    """
    return calculateCartValue(list) + Decimal(deliveryCost)