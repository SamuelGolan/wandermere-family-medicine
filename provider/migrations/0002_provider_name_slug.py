# Generated by Django 4.1.3 on 2022-11-27 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='name_slug',
            field=models.SlugField(blank=True, editable=False),
        ),
    ]
