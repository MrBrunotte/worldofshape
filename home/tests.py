from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from home.views import (
    home,
    about,
    contact,
    testimonials
)


# Create your tests here.

# urls test - run: python manage.py test home


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('main-home')
        self.assertEquals(resolve(url).func, home)

    def test_about_url_resolves(self):
        url = reverse('main-about')
        self.assertEquals(resolve(url).func, about)

    def test_contact_url_resolves(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact)

    def test_testimonials_url_resolves(self):
        url = reverse('testimonials')
        self.assertEquals(resolve(url).func, testimonials)


# views test

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('main-home')
        self.about_url = reverse('main-about')
        self.contact_url = reverse('contact')
        self.testimonials_url = reverse('testimonials')

    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_about_GET(self):
        response = self.client.get(self.about_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about.html')

    def test_contact_GET(self):
        response = self.client.get(self.contact_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact.html')

    def test_testimonials_GET(self):
        response = self.client.get(self.testimonials_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/testimonials.html')
