from django.shortcuts import render

# Create your views here.

def provider_view(request, firstname, lastname):
    return render('provider/provider.html')