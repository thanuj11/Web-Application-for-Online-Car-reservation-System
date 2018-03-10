# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-16 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0002_homemodel_search'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homemodel',
            name='dropoff',
            field=models.CharField(choices=[('clearlake', 'clearlake'), ('galveston', 'galveston'), ('highlands', 'highlands'), ('downtown', 'downtown')], max_length=20),
        ),
        migrations.AlterField(
            model_name='homemodel',
            name='pickup',
            field=models.CharField(choices=[('clearlake', 'clearlake'), ('galveston', 'galveston'), ('highlands', 'highlands'), ('downtown', 'downtown')], max_length=20),
        ),
    ]
