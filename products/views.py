from django.shortcuts import render
from .models import Program

# Create your views here.


def all_programs(request):
    programs = Program.objects.all()
    return render(request, 'products/programs.html', {'programs': programs})

"""
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
"""
