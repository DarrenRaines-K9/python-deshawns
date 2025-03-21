# Generated by Django 5.1.7 on 2025-03-17 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='Walker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('email', models.CharField(max_length=155)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='walkers', to='deshawnapi.city')),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('walker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dogs', to='deshawnapi.walker')),
            ],
        ),
    ]
