from django.urls import include, path
from . import views

urlpatterns = [
    path('<str:firstname>-<str:lastname>', views.provider_view ,name='provider')
]
