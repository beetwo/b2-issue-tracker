# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 08:59
from __future__ import unicode_literals

from django.db import migrations
import toucan.notifications

class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='mention_notification',
            field=toucan.notifications.fields.NotificationTypeField(choices=[('sms', 'Text Message (SMS)'), ('email', 'Email')], default='email', max_length=20),
        ),
    ]