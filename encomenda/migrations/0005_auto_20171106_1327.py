# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-06 12:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encomenda', '0004_auto_20171106_1326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='encomenda',
            old_name='quatidade',
            new_name='quantidade',
        ),
    ]