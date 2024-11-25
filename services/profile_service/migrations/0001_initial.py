# Generated by Django 5.0.7 on 2024-11-19 06:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Interest',
                'verbose_name_plural': 'Interests',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, to_field='uuid')),
                ('bio', models.TextField(blank=True, null=True)),
                ('location', models.CharField(max_length=100)),
                ('interest', models.ManyToManyField(blank=True, related_name='profiles', to='profile_service.interest')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]