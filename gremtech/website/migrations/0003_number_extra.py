# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-12 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20160412_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='number',
            name='extra',
            field=models.BooleanField(default=False),
        ),
    ]
