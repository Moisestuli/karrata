# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-05 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(blank=True, max_length=9, unique=True),
        ),
    ]
