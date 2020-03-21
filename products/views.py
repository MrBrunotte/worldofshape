from django.shortcuts import render
from .models import Program

# Create your views here.


def all_programs(request):
    programs = Program.objects.all()
    return render(request, 'products/programs.html', {'programs': programs})


def program_section(request):
    return render(request, 'products/programs.html', {'program_section': program_section})
