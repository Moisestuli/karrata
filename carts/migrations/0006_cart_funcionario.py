# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-09 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_cart_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='funcionario',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
