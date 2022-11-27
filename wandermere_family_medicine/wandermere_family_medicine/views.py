from django.shortcuts import render
from provider.models import Provider


def home_view(request):
    return render(request, 'wandermere_family_medicine/home.html', {'providers': Provider.objects.all})