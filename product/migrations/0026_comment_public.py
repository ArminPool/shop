# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-24 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_auto_20170921_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
