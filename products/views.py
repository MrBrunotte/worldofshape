from django.shortcuts import render
from .models import Program, Product
from .forms import WeightLossAnalysisForm

# Create your views here.


def all_products(request):
    products = Product.objects.all()
    return render(request, 'products/programs.html', {'products': products})


""" the one_program view should return an individual program when user clicks on 'read more' on the 'Our Training' 

program = request.session.get('program', {})
    program[id] = cart.get(id)

    request.session['cart'] = cart
    return redirect(reverse('program'))

"""


def one_program(request):
    program = Program.objects.find_one()
    """A View that renders an indiviual program"""
    return render(request, "products/programs.html", {'program': program})


def all_programs(request):
    programs = Program.objects.all()
    return render(request, 'products/programs.html', {'programs': programs})


def program_section(request):
    return render(request, 'products/programs.html', {'program_section': program_section})


def WeightLossAnalysis(request):
    """
    This is the weightlossanalysis form that gives the user the correct training program according to their situation
    """
    if request.method == 'POST':
        form = WeightLossAnalysisForm(request.POST)
        if form.is_valid():

            gender = form.changed_data['gender']
            current_weight = form.changed_data['current_weight']
            expected_weight_loss = form.changed_data['expected_weight_loss']
            current_age = form.changed_data['current_age']
            training_level = form.changed_data['training_level']

            print(gender, current_weight, expected_weight_loss,
                  current_age, training_level)

    form = WeightLossAnalysisForm()
    return render(request, 'products/weight_analysis.html', {'form': form})
