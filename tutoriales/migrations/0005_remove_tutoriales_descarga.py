# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-11 15:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutoriales', '0004_descargas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutoriales',
            name='descarga',
        ),
    ]
