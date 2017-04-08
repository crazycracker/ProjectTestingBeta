# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-08 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0002_auto_20170408_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('student', 'STUDENT'), ('faculty', 'FACULTY')], max_length=10, verbose_name='type'),
        ),
    ]
