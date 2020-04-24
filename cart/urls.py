from django.conf.urls import url
from .views import (
    view_cart,
    add_meal_to_cart,
    add_product_to_cart,
    adjust_product_in_cart,
    adjust_meal_in_cart,
    delete_meal_in_cart
)
urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),

    url(r'^add_meal_to_cart/(?P<id>\d+)',
        add_meal_to_cart, name='add_meal_to_cart'),

    url(r'^add_product_to_cart/(?P<id>\d+)',
        add_product_to_cart, name='add_product_to_cart'),

    url(r'^adjust_product_in_cart/(?P<id>\d+)',
        adjust_product_in_cart, name='adjust_product_in_cart'),

    url(r'^adjust_meal_in_cart/(?P<id>\d+)',
        adjust_meal_in_cart, name='adjust_meal_in_cart'),

    url(r'^delete/(?P<id>\d+)',
        delete_meal_in_cart, name='delete_meal_in_cart'),
]
