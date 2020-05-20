"""worldofshape URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url, handler403, handler404, handler500
from django.conf.urls.static import static
from users import views as user_views
from home import views as home_views
from products import views as products_views
from products import urls as urls_products
from products.views import all_products
from meals import views as meals_views
from meals import urls as urls_meals
from meals.views import all_meals
from checkout import urls as urls_checkout
from cart import urls as urls_cart
from django.views import static
from .settings import MEDIA_ROOT

handler404 = 'home.views.error_404'
handler500 = 'home.views.error_500'

urlpatterns = [
    # admin template
    path('admin/', admin.site.urls),

    # home app
    path('', include('home.urls')),

    # home app view
    path('contact/', home_views.contact, name='contact'),

    # home app view
    path('testimonials/', home_views.contact, name='testimonials'),

    # home app 404 error
    # TODO how do i make this page appear when there is a 404 error??
    path('404/', auth_views.LogoutView.as_view(template_name='home/404.html'), name='404'),

    # home app 405 error
    # TODO how do i make this page appear when there is a 404 error??
    path('405/', auth_views.LogoutView.as_view(template_name='home/405.html'), name='405'),

    # home app 500 error
    # TODO how do i make this page appear when there is a 404 error??
    path('500/', auth_views.LogoutView.as_view(template_name='home/500.html'), name='500'),

    # users app register view
    path('register/', user_views.register, name='register'),

    # users app profile view
    path('profile/', user_views.profile, name='profile'),

    # users app login view
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    # users app logout view
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # users app PasswordResetView to reset the password
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html'), name='password_reset'),

    # users app PasswordResetDoneView route for when the password request is done
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'), name='password_reset_done'),

    # users app PasswordResetConfirmView Takes two url parameters: UIDB64 and token from link in email
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),

    # users app PasswordResetCompleteView
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'), name='password_reset_complete'),

    # products app all programs
    path('programs/', include('products.urls')),

    # products app productdetail view single product
    path('program/', products_views.ProductDetailView, name='product-detail'),

    # meals app all meals
    path('meals/', include('meals.urls')),

    # meals app mealdetail view single meal
    path('meal/', meals_views.MealDetailView, name='meal-detail'),

    # products app
    path('weight_loss/', products_views.WeightLossAnalysis,
         name='weight_loss_analysis'),

    # TODO Might have to fix this! to products/
    # products app
    url(r'^$', all_products, name='index'),

    # products app
    path('products/', products_views.all_products, name='products'),

    # meals app
    path('meals/', meals_views.all_meals, name='meals'),

    # cart app
    url(r'^cart/', include(urls_cart)),

    # checkout app
    url(r'^checkout/', include(urls_checkout)),

    # media path
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]

# We use this urlpattern when we are in DEBUG mode
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# We use this urlpattern when we are in DEBUG mode
# if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL,
#                          document_root=settings.MEDIA_ROOT)
