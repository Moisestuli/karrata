# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-06 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_produto_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='upload',
            field=models.FileField(default='produtos/default.jpg', upload_to='produtos/'),
        ),
    ]
