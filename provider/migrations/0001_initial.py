# Generated by Django 4.1.3 on 2022-11-19 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=30)),
                ('degree', models.CharField(choices=[('MD', 'Doctor'), ('NP', 'Nurse Practitioner'), ('PA', 'Physicians Assistant')], max_length=2)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('bio', models.TextField(blank=True)),
            ],
        ),
    ]
