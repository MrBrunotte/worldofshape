from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from checkout.views import checkout


# Create your tests here.
# urls test - run: python manage.py test checkout


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func, checkout)
