# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0004_auto_20160614_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='homepage',
            field=models.URLField(blank=True),
        ),
    ]
