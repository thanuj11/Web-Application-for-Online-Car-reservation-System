# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-11 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup', models.CharField(choices=[('cl', 'clear lake'), ('gl', 'galveston'), ('hl', 'highlands'), ('dt', 'downtown')], max_length=20)),
                ('dropoff', models.CharField(choices=[('cl', 'clear lake'), ('gl', 'galveston'), ('hl', 'highlands'), ('dt', 'downtown')], max_length=20)),
                ('username', models.CharField(max_length=50)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searchtext', models.CharField(max_length=50)),
            ],
        ),
    ]
