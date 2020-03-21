from django.urls import path
from . import views
from .views import all_programs, program_section

urlpatterns = [
    path('', views.all_programs, name='programs'),
    path('programs/', views.all_programs, name='#program_section'),
]
