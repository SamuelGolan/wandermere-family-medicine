# Generated by Django 4.1.6 on 2023-02-12 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("provider", "0004_provider_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="provider",
            name="image",
            field=models.ImageField(
                default="static/img/default_provider.jpg", upload_to="profile_pics"
            ),
        ),
    ]
