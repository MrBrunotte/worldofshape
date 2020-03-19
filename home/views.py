from django.shortcuts import render


# Create your views here.

# home view
def home(request):
    return render(request, 'home/index.html')
