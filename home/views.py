from django.shortcuts import render


# Create your views here.


def home(request):
    """ home view takes us to our landingpage """
    return render(request, 'home/index.html')


def about(request):
    """ about view takes us to our aboutpage """
    return render(request, 'home/about.html')


def contact(request):
    """ Contact view takes us to our contactpage """
    return render(request, 'home/contact.html')


def testimonials(request):
    """ Contact view takes us to our contactpage """
    return render(request, 'home/testimonials.html')
