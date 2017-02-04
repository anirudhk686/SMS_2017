# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_tradebook_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setprice', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='stockprice',
            old_name='priceintial',
            new_name='priceinitial',
        ),
    ]
