from django.urls import path
from django.conf.urls import url, include
from . import views
from .views import (
    all_meals,
    one_meal,
    MealDetailView
)

urlpatterns = [

    path('meals/', views.all_meals, name='meals'),
    path('meal/', views.one_meal, name='meal'),
    path('meal/<int:pk>/',
         MealDetailView.as_view(), name='meal-detail'),
]
