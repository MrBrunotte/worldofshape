from django.shortcuts import get_object_or_404
from products.models import Product
from meals.models import Meal


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    total_product = 0
    product_count = 0
    total_meal = 0
    meal_count = 0

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total_product += quantity * product.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity,
                           'product': product})

    for id, quantity in cart.items():
        meal = get_object_or_404(Meal, pk=id)
        total_meal += quantity * meal.price
        meal_count += quantity

        cart_items.append({'id': id, 'quantity': quantity, 'meal': meal})

    return {'cart_items': cart_items, 'total': total, 'product_count': product_count, 'meal_count': meal_count}
