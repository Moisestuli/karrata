# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-05 16:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encomenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('quatidade', models.IntegerField(default=1)),
                ('cliente', models.ManyToManyField(to='cliente.Cliente')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
