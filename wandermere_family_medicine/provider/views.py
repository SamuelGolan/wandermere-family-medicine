from django.shortcuts import render, get_object_or_404
from .import models
# Create your views here.

def provider_view(request, firstname, lastname):
    provider = get_object_or_404(models.Provider, firstname=firstname, lastname=lastname)
    return render(request, 'provider/provider.html', vars(provider))