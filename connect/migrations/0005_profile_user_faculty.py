# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-13 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0004_auto_20170811_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_faculty',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]