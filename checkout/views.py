from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import ProductLineItem, MealLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
from meals.models import Meal
import stripe


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            total_product = 0
            total_meal = 0
            for category, values in cart.items():
                for id, quantity in values.items():
                    #print(category, values, id, quantity)
                    if category == 'meal':
                        meal = get_object_or_404(Meal, pk=id)
                        total_meal += quantity * meal.price
                        meal_line_item = MealLineItem(
                            order=order,
                            meal=meal,
                            quantity=quantity
                        )
                        meal_line_item.save()
                    else:
                        product = get_object_or_404(Product, pk=id)
                        total_product += quantity * product.price
                        product_line_item = ProductLineItem(
                            order=order,
                            product=product,
                            quantity=quantity
                        )
                        product_line_item.save()

            total_line_items = meal_line_item + product_line_item
            total_line_items.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse({'products'}, {'meals'}))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(
                request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "checkout/checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
