# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 08:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invitations', '0002_auto_20161009_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toucaninvitation',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
    ]