from django.contrib import admin
from . import models

# Register your models here.
class ProviderAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Provider, ProviderAdmin)