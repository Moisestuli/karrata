# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-06 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='upload',
            field=models.FileField(default='default.jpg', upload_to='categoria/'),
        ),
    ]