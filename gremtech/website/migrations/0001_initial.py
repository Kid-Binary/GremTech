# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-12 06:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_first', models.EmailField(max_length=254)),
                ('email_second', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('surname', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('description', models.TextField(max_length=1000, verbose_name='Биография')),
                ('photo', models.ImageField(upload_to='photos/', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Functionality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Функциональность',
                'verbose_name_plural': 'Функциональность',
            },
        ),
        migrations.CreateModel(
            name='GetInTouch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=1000, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Блок "Get In Touch"',
                'order_prefix': ' ',
                'verbose_name_plural': ' Блок "Get In Touch"',
            },
        ),
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('headline', models.CharField(max_length=200, verbose_name='Деятельность')),
                ('title', models.CharField(max_length=100, verbose_name='Название компании')),
                ('bottomline', models.CharField(max_length=200, verbose_name='Слоган')),
            ],
            options={
                'verbose_name': 'Блок "Intro"',
                'order_prefix': '    ',
                'verbose_name_plural': '    Блок "Intro"',
            },
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='Значение')),
                ('description', models.CharField(max_length=50, verbose_name='Описание')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.Employee')),
            ],
            options={
                'verbose_name': 'Цифра',
                'verbose_name_plural': 'Цифры',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visuals', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description_short', models.CharField(max_length=200, verbose_name='Краткое описание')),
                ('description_full', models.TextField(max_length=1000, verbose_name='Подробное описание')),
                ('additional', models.TextField(max_length=1000, verbose_name='Дополнительно')),
                ('stage', models.CharField(max_length=200, verbose_name='Стадия')),
                ('completion', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Готовность стадии (%)')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.Project')),
            ],
            options={
                'verbose_name': 'Cфера прменения',
                'verbose_name_plural': 'Сферы применения',
            },
        ),
        migrations.CreateModel(
            name='WeAre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('headline', models.CharField(max_length=200, verbose_name='Определение')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=1000, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Блок "We Are"',
                'order_prefix': '   ',
                'verbose_name_plural': '   Блок "We Are"',
            },
        ),
        migrations.CreateModel(
            name='WhatWeDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('text', models.TextField(max_length=1000, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Блок "What We Do"',
                'order_prefix': '  ',
                'verbose_name_plural': '  Блок "What We Do"',
            },
        ),
        migrations.AddField(
            model_name='number',
            name='we_are',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.WeAre'),
        ),
        migrations.AddField(
            model_name='functionality',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.Project'),
        ),
    ]
