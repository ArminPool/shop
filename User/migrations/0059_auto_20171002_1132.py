# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-02 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0058_auto_20171002_1109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='body',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='message',
            name='inbox',
        ),
        migrations.AddField(
            model_name='message',
            name='Issue_options',
            field=models.TextField(choices=[('co', 'همکاری'), ('pb', 'مشکل در خرید'), ('ag', 'درخواست بازی'), ('o', 'موارد دیگر')], default=('co', 'همکاری')),
        ),
    ]
