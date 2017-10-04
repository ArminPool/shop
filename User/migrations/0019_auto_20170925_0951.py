# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 06:21
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0018_auto_20170925_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_img',
            field=models.FileField(default='settings.MEDIA_ROOT/default_img_prof.jpg', storage=django.core.files.storage.FileSystemStorage(location='/armin/shop images/'), upload_to='uploaded'),
        ),
    ]
