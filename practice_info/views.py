from django.shortcuts import render, reverse
from provider.models import Provider
from django.http import JsonResponse, HttpResponseRedirect

from django.contrib import messages
from django.core.mail import send_mail


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
    try:
        send_mail(subject, message, from_email=None, recipient_list=['samuelcgolan@gmail.com',])
    except Exception as err:
        messages.add_message(messages.WARNING, "Error: There was an error sending your message.")
        print(err)
    return HttpResponseRedirect(reverse("contact"))
