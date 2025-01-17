from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view ,name='home'),
    path('about/', views.about_view ,name='about'),
    path('contact/', views.contact_view ,name='contact'),
    path('contact-email/', views.send_contact_email, name='contact_email'),
    path('schedule', views.schedule, name='schedule')
]