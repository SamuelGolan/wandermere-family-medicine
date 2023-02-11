from django.db import models
from slugify import slugify
from PIL import Image

# Create your models here.

class Provider(models.Model):
    class Degree(models.TextChoices):
        DOCTOR = "MD"
        NURSE_PRACTITIONER = "NP"
        PHYSICIANS_ASSISTANT = "PA"
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    degree = models.CharField(choices=Degree.choices, max_length=2)
    title = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    bio = models.TextField(blank=True)
    name_slug = models.SlugField(max_length=50, editable=False, blank=True)
    image = models.ImageField(blank=True, upload_to='profile_pics')

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.degree}"
    
    def save(self, *args, **kwargs):
        print("Saving Image")
        try:
            self.name_slug = slugify(f'{self.firstname} {self.lastname}', lowercase=False)
            img = Image.open(self.image.path)
            if img.width != img.height:
                print(img.height, img.width)
                if img.height > img.width:
                    print(False)
                    diff = img.height - img.width
                    img = img.crop((0, int(diff//2), img.width, int(img.height-diff//2)))
                elif img.width > img.height:
                    print(True)
                    diff = img.width - img.height
                    img = img.crop((int(diff//2), 0, int(img.width-diff//2), img.height))
                img.save(self.image.path)
            if img.height > 300 or img.width > 300:
                img.thumbnail((300, 300))
                img.save(self.image.path)
            super().save(*args, **kwargs)
        except Exception as err:
            print(err)
