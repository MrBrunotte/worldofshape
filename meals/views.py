from django.shortcuts import render
from .models import Meal, Program
from django.views.generic import DetailView

# Create your views here.


class MealDetailView(DetailView):
    model = Meal
    template_name = 'meals/meal.html'  # <app>/<model>_<view>.html


def all_meals(request):
    meals = Meal.objects.all()
    return render(request, 'meals/meals.html', {'meals': meals})


def one_meal(request):
    meal = Program.objects.find_one()
    """A View that renders an indiviual program"""
    return render(request, "meals/meal.html", {'meal': meal})
