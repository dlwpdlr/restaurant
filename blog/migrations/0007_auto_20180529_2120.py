# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-29 12:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180529_2104'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='About',
            new_name='AboutStore',
        ),
    ]
