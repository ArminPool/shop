# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-24 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_auto_20170924_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_img',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
