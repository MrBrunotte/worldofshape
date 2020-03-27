from django.urls import path
from . import views
from .views import all_programs, program_section, WeightLossAnalysisForm

urlpatterns = [
    path('', views.all_programs, name='programs'),
    path('programs/', views.all_programs, name='#program_section'),
    path('weight_loss/', views.WeightLossAnalysis, name='weight_loss'),
]
