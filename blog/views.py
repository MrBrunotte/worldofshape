from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'StefanB',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 13, 2020'
    },
    {
        'author': 'Rebecca',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 13, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'About'})
