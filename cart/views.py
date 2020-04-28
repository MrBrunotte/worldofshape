from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product
from meals.models import Meal

# Create your views here.


def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart/cart.html")

# products.html/product.html/meals.html


def add_product_to_cart(request, id):
    """
    Add a training program to cart based on its ID. 
    One program is added.
    If cart is empty create two dict ‘meal’ and ‘product’, if items in cart they are added to the dict
    If the product already exists in cart add quantity (1)
    Else add one product to cart
    Put new product in cart
    Redirect user to cart template
    """
    quantity = 1

    cart = request.session.get('cart', {'meal': {}, 'product': {}})
    #print(cart, id)
    if id in cart['product']:
        cart['product'][id] = int(cart['product'][id]) + quantity
    else:
        cart['product'][id] = quantity

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def add_meal_to_cart(request, id):
    """
    Add a meal to cart based on its ID. 
    One meal is added.
    If cart is empty create two dict ‘meal’ and ‘product’, if items in cart they are added to the dict
    If the meal already exists in cart add quantity (1)
    Else add one meal to cart
    Put new meal in cart
    Redirect user to cart template
    """
    quantity = 1

    cart = request.session.get('cart', {'meal': {}, 'product': {}})
    if id in cart['meal']:
        cart['meal'][id] = int(cart['meal'][id]) + quantity
    else:
        cart['meal'][id] = quantity

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

# cart.html


def update_product_item(request, id):

    cart = request.session.get('cart', {'product'})
    quantity = int(request.POST.get({'quantity'}))
    print('quantity')
    if quantity in cart > 0:
        cart['product'][id] = quantity
    else:
        cart.pop(id)
    print(cart, id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def update_meal_item(request, id):

    cart = request.session.get('cart', ('meal', {'quantity'}))
    # print(cart)
    quantity = int(request.POST.get('quantity'))
    #print('meal', {quantity})

    if quantity in cart > 0:
        cart['meal'][id] = quantity
        print(cart)
    else:
        cart.pop(quantity)
    print(quantity)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def delete_meal_item(request, id):
    """Delete a meal in the cart"""

    cart = request.session.get('meal', {id})
    cart.remove('meal', {id})
    messages.success(
        request, f'Your recipe/mealplan has been deleted from your cart!')
    return redirect(reverse('view_cart'))


def delete_product_item(request, id):
    """Delete a product in the cart"""

    cart = request.session.get('meal', {id})
    cart.remove('meal', {id})
    messages.success(
        request, f'Your recipe/mealplan has been deleted from your cart!')
    return redirect(reverse('view_cart'))


"""
def remove_product(request, id):
    cart = view_cart(request)
    product = get_object_or_404(Product, pk=id)
    cart.remove(product)
    return redirect(reverse('view_cart'))

def remove_meal(request, id):
    cart = view_cart(request)
    meal = get_object_or_404(Meal, pk=id)
    cart.remove(meal)
    return redirect(reverse('view_cart'))
"""
