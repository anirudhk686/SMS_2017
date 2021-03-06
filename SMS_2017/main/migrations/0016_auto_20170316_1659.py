# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20170225_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_control',
            name='total_teams',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='net_worth',
            field=models.IntegerField(default=10000),
        ),
        migrations.AlterField(
            model_name='team',
            name='money',
            field=models.IntegerField(default=10000),
        ),
    ]
