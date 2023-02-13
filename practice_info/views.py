from django.shortcuts import render
from django.urls import reverse_lazy, reverse
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
        send_mail(
            subject, 
            f"Name: {name} Email: {email} Message: {message}", 
            from_email=None, recipient_list=['agolan@wandemere-medicine.com',]
        )
        messages.add_message(request, messages.SUCCESS, "Message sent")
    except Exception as err:
        print(err)
        messages.add_message(request, messages.ERROR, "There was an error sending your message.")
    try:
        return HttpResponseRedirect(reverse("contact"))
    except Exception as err:
        print(err)


def schedule(request):
    return render(request, 'practice_info/schedule_appointment.html', {'providers': Provider.objects.all})