from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),                 #from home view
    path('about/', views.about, name='main-about'),         #from about view
]
