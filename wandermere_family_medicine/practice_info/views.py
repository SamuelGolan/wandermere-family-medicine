from django.shortcuts import render
from provider.models import Provider


def home_view(request):
    return render(request, 'practice_info/home.html', {'providers': Provider.objects.all})