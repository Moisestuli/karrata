# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 13:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtos', '0002_produto_fornecedores'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cliente', models.CharField(max_length=255, unique=True)),
                ('quantidade', models.IntegerField(default=1)),
                ('ultimo_pagamento', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('primeria_compra', models.DateTimeField(auto_now_add=True)),
                ('ultima_compra', models.DateTimeField(auto_now=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.Produto')),
            ],
            options={
                'verbose_name_plural': 'Vendas',
            },
        ),
    ]
