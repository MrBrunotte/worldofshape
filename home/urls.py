from django.urls import path
from . import views
from .views import home, about, contact

urlpatterns = [
    path('', views.home, name='main-home'),  # from home view
    path('about/', views.about, name='main-about'),  # from about view
    path('contact/', views.contact, name='contact'),  # from contact view
]
