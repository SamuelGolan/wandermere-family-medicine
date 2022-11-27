from django.urls import include, path
from . import views

urlpatterns = [
    path('<str:name_slug>', views.provider_view ,name='provider')
]
