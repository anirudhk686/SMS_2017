# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20170122_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradebook',
            name='num',
            field=models.IntegerField(default=0),
        ),
    ]
