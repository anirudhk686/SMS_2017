# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20170124_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockLeft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left', models.IntegerField()),
                ('team_no', models.IntegerField()),
                ('stockname', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='stockleft',
            unique_together=set([('stockname', 'team_no')]),
        ),
    ]