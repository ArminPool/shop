# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 18:09
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0038_auto_20170925_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='pro_img',
            field=models.ImageField(default='shop/media/default_img_prof.jpg', storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\armin\\shop\\shop/media'), upload_to='uploaded'),
        ),
    ]
