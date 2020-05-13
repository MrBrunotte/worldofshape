from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from meals.views import (
    all_meals,
    MealDetailView
)
from products.views import (
    all_products,
    all_programs,
    one_program,
    ProductDetailView
)
from products.models import Product, Program
from meals.models import Meal
import json

# Create your tests here.

# urls test - run: python manage.py test products


class TestUrls(SimpleTestCase):

    def test_products_url_resolves(self):
        url = reverse('products')
        self.assertEquals(resolve(url).func, all_products)

    def test_programs_url_resolves(self):
        url = reverse('programs')
        self.assertEquals(resolve(url).func, all_programs)

    def test_program_url_resolves(self):
        url = reverse('program')
        self.assertEquals(resolve(url).func, one_program)

    def test_meals_url_resolves(self):
        url = reverse('meals')
        self.assertEquals(resolve(url).func, all_meals)

    def test_project_detail_url_resolves(self):
        url = reverse('product-detail')
        self.assertEquals(resolve(url).func, ProductDetailView)

    def test_meal_detail_url_resolves(self):
        url = reverse('meal-detail')
        self.assertEquals(resolve(url).func, MealDetailView)


# views test

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.products_url = reverse('products')
        self.meals_url = reverse('meals')
        self.programs_url = reverse('programs')

    def test_all_products_GET(self):
        response = self.client.get(self.products_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/programs.html')

    def test_all_meals_GET(self):
        response = self.client.get(self.meals_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'meals/meals.html')

    def test_all_program_GET(self):
        response = self.client.get(self.programs_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/programs.html')
