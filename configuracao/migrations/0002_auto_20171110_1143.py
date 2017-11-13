# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-10 10:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('configuracao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracao',
            name='imagem',
            field=models.FileField(default='profile/default.jpg', upload_to='profile/'),
        ),
        migrations.AddField(
            model_name='configuracao',
            name='perfil',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]