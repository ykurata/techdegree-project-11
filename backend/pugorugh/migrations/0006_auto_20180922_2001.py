# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2018-09-22 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pugorugh', '0005_auto_20180921_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdog',
            name='status',
            field=models.CharField(choices=[('l', 'Liked'), ('d', 'Disliked')], max_length=1),
        ),
    ]
