# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-22 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170122_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='id1',
            field=models.CharField(default='', max_length=12, verbose_name='Paritcipant 1 ID'),
        ),
        migrations.AlterField(
            model_name='team',
            name='id2',
            field=models.CharField(default='', max_length=12, verbose_name='Paritcipant 2 ID'),
        ),
    ]
