from django.shortcuts import render, get_object_or_404
from slugify import slugify
from .import models
# Create your views here.

def provider_view(request, name_slug):
    provider = get_object_or_404(models.Provider, name_slug=name_slug)
    return render(request, 'provider/provider.html', {'provider': provider, 'providers': models.Provider.objects.all})