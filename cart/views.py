from django.shortcuts import render, redirect, reverse

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
    print(cart)
    return redirect(reverse('view_cart'))


def add_meal_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = 1

    cart = request.session.get('cart', {})
    cart['meal'] = cart.get('meal', {id: quantity})

    request.session['cart'] = cart
    print(cart)
    return redirect(reverse('view_cart'))


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    # todo If nothing is selected as new qty
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
