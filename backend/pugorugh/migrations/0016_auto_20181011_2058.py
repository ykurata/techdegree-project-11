# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-11 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pugorugh', '0015_auto_20181010_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdog',
            name='status',
            field=models.CharField(choices=[('l', 'Liked'), ('d', 'Disliked'), ('u', 'Undecided')], max_length=10),
        ),
    ]