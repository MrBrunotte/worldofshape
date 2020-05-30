from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def home(request):
    """ home view takes us to our landingpage """
    return render(request, 'home/index.html')


def about(request):
    """ about view takes us to our aboutpage """
    return render(request, 'home/about.html')


def contact(request):
    """ Contact view takes us to our contactpage """
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            'Message from ' + message_name,  # subject
            message,  # Email message
            message_email,  # Email is sent from
            ['mrbrunotte@gmail.com'],  # Email goes to
        )

        return render(request, 'home/contact.html',
                      {'message_name': message_name})

    else:
        return render(request, 'home/contact.html')


def testimonials(request):
    """ Contact view takes us to our contactpage """
    return render(request, 'home/testimonials.html')


def error_403(request, exception):
    """
    Render the World of Shape 403.html error page
    """
    return render(request, 'home/403.html')


def error_404(request, exception):
    """
    Render the World of Shape 404.html error page
    """
    return render(request, 'home/404.html')


def error_500(request):
    """
    Render the World of Shape 500.html page
    """
    return render(request, 'home/500.html')
