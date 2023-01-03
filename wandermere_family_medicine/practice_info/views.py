from django.shortcuts import render
from provider.models import Provider


def home_view(request):
    return render(request, 'practice_info/home.html', {'providers': Provider.objects.all})


def about_view(request):
    return render(request, 'practice_info/about.html', {'providers': Provider.objects.all})

def contact_view(request):
    return render(request, 'practice_info/contact.html', {'providers': Provider.objects.all})