from django.urls import path
from django.conf.urls import url, include
from . import views
from .views import (
    all_programs,
    program_section,
    WeightLossAnalysisForm,
    all_products,
    all_meals,
    one_program,
    ProductDetailView,
    MealDetailView
)

urlpatterns = [
    path('', views.all_programs, name='programs'),
    path('program/', views.one_program, name='program'),
    path('programs/', views.all_programs, name='#program_section'),
    path('weight_loss/', views.WeightLossAnalysis, name='weight_loss'),
    path('products/', views.all_products, name='products'),
    path('product/<int:pk>/',
         ProductDetailView.as_view(), name='product-detail'),
    path('meal/<int:pk>/',
         MealDetailView.as_view(), name='meal-detail'),
    path('meals/', views.all_meals, name='meals'),
]
