# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-29 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
