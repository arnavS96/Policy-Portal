# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-29 12:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team_register', '0006_auto_20170529_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='team_admin',
        ),
    ]