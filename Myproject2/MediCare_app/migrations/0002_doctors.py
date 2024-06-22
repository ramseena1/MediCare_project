# Generated by Django 5.0.6 on 2024-06-15 11:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MediCare_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='doctor', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Name', models.CharField(max_length=255)),
                ('Speciality', models.CharField(max_length=100)),
                ('Area_of_expertise', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('Document', models.ImageField(upload_to='hospital')),
                ('Approve_status', models.IntegerField(default=0)),
            ],
        ),
    ]
