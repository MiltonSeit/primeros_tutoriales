# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-11 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutoriales', '0002_auto_20160611_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutoriales',
            name='descarga',
            field=models.URLField(blank=True, null=True),
        ),
    ]