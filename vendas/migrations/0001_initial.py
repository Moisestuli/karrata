# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_client', models.CharField(max_length=255, unique=True)),
                ('telefone', models.IntegerField(blank=True)),
                ('cidade', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('no_compras', models.IntegerField(default=1)),
                ('ult_troco', models.FloatField(default=0.0)),
                ('ult_valor', models.FloatField(default=0.0)),
                ('ult_compra', models.FloatField(default=0.0)),
                ('total_compra', models.FloatField(default=0.0)),
                ('total_troco', models.FloatField(default=0.0)),
                ('total_valor', models.FloatField(default=0.0)),
                ('prim_dia_compra', models.DateTimeField(auto_now_add=True)),
                ('ult_dia_compra', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
