# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 01:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0002_dojo_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dojo',
            name='desc',
        ),
    ]
