from django.template.defaultfilters import register
from django import template
from decimal import *

@register.filter
def fromDictGetItemAttribute(dictionary, itemAttribute):
    itemAttribute = itemAttribute.split(',')
    item = dictionary.get(itemAttribute[0])
    if hasattr(item, itemAttribute[1]):
        return getattr(item, itemAttribute[1])
    else:
        return None

@register.filter
def fromDictGetItemValue(dictionary, itemName):
    return dictionary.get(itemName)

@register.filter
def calculateCartItemValue(dictionary):
    product = dictionary.get('product')
    quantity = dictionary.get('quantity')
    return product.Price * quantity

@register.filter
def getProductNum(list):
    quantity = 0
    for item in list:
        quantity = quantity + item.get('quantity')
    return quantity

@register.filter
def calculateCartValue(list):
    value = 0
    for item in list:
        product = item.get('product')
        value = value + (product.Price * item.get('quantity'))
    return value

@register.filter
def calculateCartFinalValue(list, deliveryCost):
    return calculateCartValue(list) + Decimal(deliveryCost)