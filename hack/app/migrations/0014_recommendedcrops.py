# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-12 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20171112_0645'),
    ]

    operations = [
        migrations.CreateModel(
            name='recommendedCrops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=18)),
                ('season', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=30)),
            ],
        ),
    ]
