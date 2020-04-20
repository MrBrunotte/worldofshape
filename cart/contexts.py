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

    for category, values in cart.items():
        for id, quantity in values.items():
            if category == 'meal':
                meal = get_object_or_404(Meal, pk=id)
                total_meal += quantity * meal.price
                meal_count += quantity
                cart_items.append(
                    {'id': id, 'quantity': quantity, 'meal': meal})
            else:
                product = get_object_or_404(Product, pk=id)
                total_product += quantity * product.price
                product_count += quantity
                cart_items.append({'id': id, 'quantity': quantity,
                                   'product': product})

    return {'cart_items': cart_items, 'total': total_meal + total_product, 'product_count': product_count, 'meal_count': meal_count, 'all_items_in_cart': meal_count + product_count}
