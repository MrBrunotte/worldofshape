from django.urls import path
from . import views
from .views import all_programs

urlpatterns = [
    path('', views.all_programs, name='programs'),
]
