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
from django.conf.urls import url
from django.conf.urls.static import static
from users import views as user_views
from home import views as home_views
from products import views as products_views
from products import urls as urls_products
from products.views import all_products
from checkout import urls as urls_checkout
from cart import urls as urls_cart
from search import urls as urls_search
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    # admin template
    path('admin/', admin.site.urls),

    # home app
    path('', include('home.urls')),

    # users app register view
    path('register/', user_views.register, name='register'),

    # users app profile view
    path('profile/', user_views.profile, name='profile'),

    # home app view
    path('contact/', home_views.contact, name='contact'),

    # home app view
    path('testimonials/', home_views.contact, name='testimonials'),

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

    # products app
    path('programs/', include('products.urls')),

    # products app productdetail view
    path('program/', products_views.ProductDetailView, name='product-detail'),

    # products app Individual program
    # path('program/', include('products.urls')),
    # products app
    path('weight_loss/', products_views.WeightLossAnalysis,
         name='weight_loss_analysis'),

    # Might have to fix this! to products/
    #url('r^$', all_products, name='index'),
    url(r'^$', all_products, name='index'),

    # products/
    path('products/', products_views.all_products, name='products'),

    # cart
    url(r'^cart/', include(urls_cart)),

    # search
    url(r'^search/', include(urls_search)),

    # checkout
    url(r'^checkout/', include(urls_checkout)),

    # media path
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),

    # blog app
    path('blog/', include('blog.urls')),
]

# We use this urlpattern when we are in DEBUG mode, We will us AWS S3 Bucket in production
# if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL,
#                          document_root=settings.MEDIA_ROOT)
