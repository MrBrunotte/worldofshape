from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from cart.views import (
    view_cart,
    add_to_cart,
    adjust_cart
)


# Create your tests here.

# urls test - run: python manage.py test cart


class TestUrls(SimpleTestCase):

    def test_view_cart_url_resolves(self):
        url = reverse('view_cart')
        self.assertEquals(resolve(url).func, view_cart)


# views test

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.cart_url = reverse('view_cart')

    def test_view_cart_GET(self):
        response = self.client.get(self.cart_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')
