from django.shortcuts import render
from provider.models import Provider
from django.http import JsonResponse

from .forms import ContactForm


def home_view(request):
    return render(request, 'practice_info/home.html', {'providers': Provider.objects.all})


def about_view(request):
    return render(request, 'practice_info/about.html', {'providers': Provider.objects.all})


def contact_view(request):
    # data = {'name': 'Your Name', 'email': 'Your Email', 'subject': 'Subject', 'message': 'Message'}
    form = ContactForm()
    return render(request, 'practice_info/contact.html', {'providers': Provider.objects.all, 'form': form})


def send_contact_email(request):
    form = request.POST
    print(form)
    subject = form['subject']
    email = form['email']
    message = form['message']
    name = form['name']

    return JsonResponse({'subject': subject, 'email': email, 'message': message, 'name': name})
