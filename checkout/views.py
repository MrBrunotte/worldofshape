from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import ProgramLineItem, MealLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
from meals.models import Meal
import stripe


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET


def check_input_fields(request, order_form):
    """
    Creates the form to fill in the data for the payment
    """
    lastName = order_form['last_name'].value()
    firstName = order_form['first_name'].value()
    phoneNumber = order_form['phone_number'].value()
    country = order_form['country'].value()
    streetAddress1 = order_form['street_address1'].value()
    townOrCity = order_form['town_or_city'].value()

    if lastName is None or lastName == "":
        messages.error(request, 'first name is required')
        return False
    if firstName is None or firstName == "":
        messages.error(request, 'last name is required')
        return False
    if streetAddress1 is None or streetAddress1 == "":
        messages.error(request, 'street name is required')
        return False
    if townOrCity is None or townOrCity == "":
        messages.error(request, 'Town or city is required')
        return False
    if country is None or country == "":
        messages.error(request, 'Country is required')
        return False
    if phoneNumber is None or phoneNumber == "":
        messages.error(request, 'Phone number is required')
        return False

    return True


@login_required()
def checkout(request):
    """
    This method gets the posted data in the orderform and pyamentform.
    If both forms are ok it is saved in order
    it then gets the cart content and assigns the valut to cart,
    it creates three starting variabls.
    A outer for loops gets the categori
    """
    if request.method == "POST":
        order_form = OrderForm(request.POST)

        if check_input_fields(request, order_form) is False:
            payment_form = MakePaymentForm()
            return render(request, "checkout/checkout.html",
                          {"order_form": order_form,
                           "payment_form": payment_form,
                           "publishable": settings.STRIPE_PUBLISHABLE})

        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {"meal": {}, "program": {}})

            total = 0
            total_product = 0
            total_meal = 0
            cart_products = 0
            product_quantity = 0
            meal_quantity = 0

            for category, values in cart.items():

                for id, quantity in values.items():

                    if category == 'meal':
                        meal = get_object_or_404(Meal, pk=id)
                        total_meal += quantity * meal.price
                        meal_line_item = MealLineItem(
                            order=order,
                            meal=meal,
                            quantity=quantity,
                        )
                        meal_line_item.save()

                    if category == 'product':
                        product = get_object_or_404(Product, pk=id)
                        total_product += quantity * product.price
                        program_line_item = ProgramLineItem(
                            order=order,
                            program=product,
                            quantity=quantity,
                        )
                        program_line_item.save()

            total = total_meal + total_product

            print(total)

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="SEK",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.success(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('main-home'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(
                request, "We were unable to take a payment with that card!")
    else:
        cart = request.session.get('cart', {"meal": {}, "product": {}})
        if cart['meal'] == {} and cart['product'] == {}:
            messages.error(
                request, "Your cart is empty, please add items to checkout")
            return redirect(reverse('products'))
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "checkout/checkout.html",
                  {'order_form': order_form, 'payment_form': payment_form,
                   'publishable': settings.STRIPE_PUBLISHABLE})
