# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-11 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0002_auto_20170809_0345'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='hobby_question',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='subject_interest_question',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
