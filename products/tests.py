from django.test import TestCase
from .models import Product


# Create your tests here.

class ProductTest(TestCase):
    """
    Here we will define the tests that we will run against our Product models
    test will fail in 'A product' doesnt match 'A procuct'
    """

    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')
