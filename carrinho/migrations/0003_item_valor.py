# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0002_auto_20170829_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=18, verbose_name='valor'),
        ),
    ]
