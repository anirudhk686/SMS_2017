# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_no', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('password', models.PositiveSmallIntegerField(max_length=2)),
                ('member1', models.CharField(max_length=8)),
                ('member2', models.CharField(default='NONE', max_length=8)),
                ('money', models.PositiveIntegerField(default=1000000)),
            ],
        ),
        migrations.DeleteModel(
            name='Teaminfo',
        ),
    ]