# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 13:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_config', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='siteconfig',
            options={'verbose_name': 'Site Config'},
        ),
    ]
