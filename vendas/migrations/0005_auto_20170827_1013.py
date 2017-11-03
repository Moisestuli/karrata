# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0004_auto_20170827_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='total_compra',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='venda',
            name='total_troco',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]
