# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0003_item_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=18, verbose_name='valor'),
        ),
    ]
