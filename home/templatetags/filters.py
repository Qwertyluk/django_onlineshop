from django.template.defaultfilters import register

@register.filter
def getSetFromManyToOneRelationship(_object, setName):
    _set = getattr(_object, setName)
    return _set.all()

@register.filter
def calculateTotalOrderPrice(order):
    orderElements = order.orderelement_set.all()
    sum = 0
    for orderElement in orderElements:
        sum = sum + (orderElement.product.Price * orderElement.quantity)

    return sum
    
    