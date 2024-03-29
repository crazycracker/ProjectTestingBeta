# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-08 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0005_auto_20170408_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='air_conditioner',
            field=models.BooleanField(choices=[(True, 'WORKING'), (False, 'NOT WORKING')], max_length=20, verbose_name='AC condition'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='computer',
            field=models.BooleanField(choices=[(True, 'WORKING'), (False, 'NOT WORKING')], max_length=20, verbose_name='Computer condition'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='projector',
            field=models.BooleanField(choices=[(True, 'WORKING'), (False, 'NOT WORKING')], max_length=20, verbose_name='Projector condition'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='speakers',
            field=models.BooleanField(choices=[(True, 'WORKING'), (False, 'NOT WORKING')], max_length=20, verbose_name='Speakes condition'),
        ),
        migrations.AlterField(
            model_name='labs',
            name='air_conditioner',
            field=models.BooleanField(choices=[(True, 'WORKING'), (False, 'NOT WORKING')], max_length=20, verbose_name='AC condition'),
        ),
    ]
