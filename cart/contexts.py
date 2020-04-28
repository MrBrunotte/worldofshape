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
    total_meal = 0
    product_quantity = 0
    meal_quantity = 0

    for category, values in cart.items():
        for id, quantity in values.items():
            #print(category, values, id, quantity)
            if category == 'meal':
                meal = get_object_or_404(Meal, pk=id)
                total_meal += quantity * meal.price
                meal_quantity += quantity
                cart_items.append(
                    {'id': id, 'meal_quantity': meal_quantity, 'meal': meal})
            else:
                product = get_object_or_404(Product, pk=id)
                total_product += quantity * product.price
                product_quantity += quantity
                cart_items.append(
                    {'id': id, 'product_quantity': product_quantity, 'product': product})

    total_cart_items = meal_quantity + product_quantity

    #print(cart_items)
    #print(total_cart_items)

    return {'cart_items': cart_items, 'total': total_meal + total_product, 'product_quantity': product_quantity, 'meal_quantity': meal_quantity, 'total_cart_items': total_cart_items}
