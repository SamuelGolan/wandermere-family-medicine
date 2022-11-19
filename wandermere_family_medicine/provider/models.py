from django.db import models

# Create your models here.

class Provider(models.Model):
    class Degree(models.TextChoices):
        DOCTOR = "MD"
        NURSE_PRACTITIONER = "NP"
        PHYSICIANS_ASSISTANT = "PA"
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    degree = models.CharField(choices=Degree.choices, max_length=2)
    email = models.EmailField(blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.degree}"
