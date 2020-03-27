from django.urls import path
from django.conf.urls import url, include
from . import views
from .views import all_programs, program_section, WeightLossAnalysisForm, all_products

urlpatterns = [
    path('', views.all_programs, name='programs'),
    path('programs/', views.all_programs, name='#program_section'),
    path('weight_loss/', views.WeightLossAnalysis, name='weight_loss'),
    path('products/', views.all_products, name='products'),
]
