# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-13 10:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(blank=True, max_length=255, null=True)),
                ('preco', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9)),
                ('quantidade', models.IntegerField(default=1)),
                ('valor_entregar', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9)),
                ('troco', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('funcionario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
