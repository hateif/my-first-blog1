# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-13 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
