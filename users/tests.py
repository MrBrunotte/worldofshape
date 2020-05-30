from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from users.views import register
from django.contrib.auth.models import User

"""
run with:
coverage run --source='users' manage.py test && coverage report &&
coverage html
Go to the folder 'htmlcov' and open 'index.html' in the browser.
Go to the htmlcov file and run the index file to get the report.
coverage report -m   To see missing lines
pytest -v --cov=users
and:      python manage.py test users
"""


class TestUrls(SimpleTestCase):

    def test_products_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)


class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.user = {
            'username': 'username',
            'email': 'testemail@gmail.com',
            'password1': 'testing321',
            'password2': 'testing321',
        }
        self.user_invalid_password = {
            'username': 'username',
            'email': 'testemail@gmail.com',
            'password1': 'test',
            'password2': 'test',
        }
        self.user_no_match_password = {
            'username': 'username',
            'email': 'testemail@gmail.com',
            'password1': 'testing321',
            'password2': '321testing',
        }
        self.user_invalid_email = {
            'username': 'username',
            'email': 'testemailgmail.com',
            'password1': 'testing321',
            'password2': '321testing',
        }

        return super().setUp()


class RegisterTest(BaseTest):
    def test_can_view_page_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_can_register_user(self):
        response = self.client.post(
            self.register_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 302)

    def test_cant_register_with_invalid_password(self):
        response = self.client.post(
            self.register_url, self.user_invalid_password, format='text/html')
        self.assertEqual(response.status_code, 200)

    def test_cant_register_with_not_matching_passwords(self):
        response = self.client.post(
            self.register_url, self.user_no_match_password, format='text/html')
        self.assertEqual(response.status_code, 200)

    def test_cant_register_with_invalid_email(self):
        response = self.client.post(
            self.register_url, self.user_invalid_email, format='text/html')
        self.assertEqual(response.status_code, 200)

    def test_cant_register_with_taken_email(self):
        self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.post(
            self.register_url, self.user_invalid_email, format='text/html')
        self.assertEqual(response.status_code, 200)


class LoginTest(BaseTest):
    def test_can_access_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_login_success(self):
        self.client.post(self.register_url, self.user, format='text/html')
        user = User.objects.filter(email=self.user['email']).first()
        user.is_active = True
        user.save()
        response = self.client.post(
            self.login_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 200)

    def test_cant_login(self):
        self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.post(
            self.login_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 200)

    def test_cant_login_with_no_username(self):
        response = self.client.post(
            self.login_url, {'password': 'passworddd', 'username': ''},
            format='text/html')
        self.assertEqual(response.status_code, 200)

    def test_cant_login_with_no_password(self):
        response = self.client.post(
            self.login_url, {'username': 'passworddd', 'password': ''},
            format='text/html')
        self.assertEqual(response.status_code, 200)
