from django.shortcuts import render
from django.contrib import messages
from .models import Program, Product
from .forms import WeightLossAnalysisForm
from django.views.generic import DetailView

# Create your views here.


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/program.html'  # <app>/<model>_<view>.html


def all_products(request):
    products = Product.objects.all()
    return render(request, 'products/programs.html', {'products': products})


def all_programs(request):
    programs = Program.objects.all()
    return render(request, 'products/programs.html', {'programs': programs})


def one_program(request):
    program = Program.objects.find_one()
    """A View that renders an indiviual program"""
    return render(request, "products/programs.html", {'program': program})


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

        else:
            messages.success(
                request, f'Something went wrong, please try again!')

    form = WeightLossAnalysisForm()
    return render(request, 'products/weight_analysis.html', {'form': form})


def correct_program(request):
    """
    This is the weightlossanalysis form that gives the user the correct training program according to their situation
    """

    correct_products = []
    form = WeightLossAnalysisForm(request.POST)

    print('xxxxx', request.POST.get('gender'))
    if (request.POST.get('gender') == 'woman') & (request.POST.get('training_level') == 'lev_1'):
        correct_products.append(Product.objects.get(id=16))
        correct_products.append(Product.objects.get(id=9))
        messages.success(
            request, f'These are the programs that suite you the best!')
        return render(request, 'products/correct_program.html', {'correct_products': correct_products})

    elif (request.POST.get('gender') == 'woman') & (request.POST.get('training_level') == 'lev_2'):
        correct_products.append(Product.objects.get(id=15))
        messages.success(
            request, f'These are the programs that suite you the best!')
        return render(request, 'products/correct_program.html', {'correct_products': correct_products})

    elif (request.POST.get('gender') == 'woman') & (request.POST.get('training_level') == 'lev_3'):
        correct_products.append(Product.objects.get(id=15))
        correct_products.append(Product.objects.get(id=4))
        correct_products.append(Product.objects.get(id=5))
        messages.success(
            request, f'These are the programs that suite you the best!')
        return render(request, 'products/correct_program.html', {'correct_products': correct_products})

    elif (request.POST.get('gender') == 'woman') & (request.POST.get('training_level') == 'lev_4'):
        correct_products.append(Product.objects.get(id=14))
        correct_products.append(Product.objects.get(id=5))
        correct_products.append(Product.objects.get(id=8))
        messages.success(
            request, f'These are the programs that suite you the best!')
        return render(request, 'products/correct_program.html', {'correct_products': correct_products})

    elif (request.POST.get('gender') == 'woman') & (request.POST.get('training_level') == 'lev_5'):
        correct_products.append(Product.objects.get(id=5))
        correct_products.append(Product.objects.get(id=6))
        correct_products.append(Product.objects.get(id=7))
        messages.success(
            request, f'These are the programs that suite you the best!')
        return render(request, 'products/correct_program.html', {'correct_products': correct_products})

    elif (request.POST.get('gender') == 'man') & (request.POST.get('training_level') == 'lev_1'):
        correct_products.append(Product.objects.get(id=16))
        correct_products.append(Product.objects.get(id=9))
        messages.success(
            request, f'These are the programs that suite you the best!')
        return render(request, 'products/correct_program.html', {'correct_products': correct_products})

    elif (request.POST.get('gender') == 'man') & (request.POST.get('training_level') == 'lev_2'):
        correct_products.append(Product.objects.get(id=15))
        correct_products.append(Product.objects.get(id=4))
        correct_products.append(Product.objects.get(id=5))
        messages.success(
            request, f'These are the programs that suite you the best!')
        return render(request, 'products/correct_program.html', {'correct_products': correct_products})

    elif (request.POST.get('gender') == 'man') & (request.POST.get('training_level') == 'lev_3'):
        correct_products.append(Product.objects.get(id=14))
        correct_products.append(Product.objects.get(id=5))
        correct_products.append(Product.objects.get(id=8))
        messages.success(
            request, f'These are the programs that suite you the best!')
        return render(request, 'products/correct_program.html', {'correct_products': correct_products})

    else:
        messages.success(
            request, f'Something went wrong, please try again!')
        return render(request, 'products/weight_analysis.html', {'form': form})
