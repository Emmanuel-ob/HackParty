# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-28 14:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_mgr', '0002_auto_20170623_0537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='displayStatus',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profession',
        ),
    ]