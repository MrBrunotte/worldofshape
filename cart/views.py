from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.


def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart/cart.html")


def add_product_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = 1

    cart = request.session.get('cart', {})
    cart['product'] = cart.get('product', {id: quantity})

    request.session['cart'] = cart
    messages.success(request, f'The program has been added to the cart!')
    return redirect(reverse('view_cart'))


def add_meal_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = 1

    cart = request.session.get('cart', {})
    cart['meal'] = cart.get('meal', {id: quantity})

    request.session['cart'] = cart
    messages.success(
        request, f'Your recipe/mealplan has been added to the cart!')
    return redirect(reverse('view_cart'))


def adjust_meal_in_cart(request, id):
    """
    Adjust the quantity of the specified product to the specific amount
    """
    quantity = int(request.POST.get('meal', {id: quantity}))
    cart = cart.get('meal', {id: quantity})

    if quantity > 0:
        cart[{id}] = quantity
    else:
        cart.pop({id: quantity})

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def delete_meal_in_cart(request, id):
    """Delete a meal in the cart"""

    cart = request.session.get('meal', {id})
    cart.remove('meal', {id})
    messages.success(
        request, f'Your recipe/mealplan has been deleted from your cart!')
    return redirect(reverse('view_cart'))
