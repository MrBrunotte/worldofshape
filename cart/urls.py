from django.conf.urls import url
from .views import (
    view_cart,
    add_meal_to_cart,
    add_product_to_cart,
    update_product_item,
    update_meal_item,
    delete_meal_item,
    delete_product_item
)
urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),

    url(r'^add_meal_to_cart/(?P<id>\d+)',
        add_meal_to_cart, name='add_meal_to_cart'),

    url(r'^add_product_to_cart/(?P<id>\d+)',
        add_product_to_cart, name='add_product_to_cart'),

    url(r'^update_product_item/(?P<id>\d+)',
        update_product_item, name='update_product_item'),

    url(r'^update_meal_item/(?P<id>\d+)',
        update_meal_item, name='update_meal_item'),

    url(r'^delete_meal_item/(?P<id>\d+)',
        delete_meal_item, name='delete_meal_item'),

    url(r'^delete_product_item/(?P<id>\d+)',
        delete_product_item, name='delete_product_item'),
]
