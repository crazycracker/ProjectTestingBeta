# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-08 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='enrollment_number',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=10, verbose_name='id'),
        ),
    ]