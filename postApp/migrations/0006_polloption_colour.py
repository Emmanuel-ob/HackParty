# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-28 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postApp', '0005_auto_20170628_0453'),
    ]

    operations = [
        migrations.AddField(
            model_name='polloption',
            name='colour',
            field=models.CharField(default='green', max_length=20),
        ),
    ]