# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-12 06:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0002_auto_20160318_1726'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='metadata',
            options={'verbose_name': 'Метаданные', 'verbose_name_plural': 'Метаданные'},
        ),
    ]
