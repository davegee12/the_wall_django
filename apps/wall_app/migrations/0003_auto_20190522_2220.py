# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-05-22 22:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall_app', '0002_auto_20190522_2145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='user',
            new_name='commenter',
        ),
        migrations.RenameField(
            model_name='messages',
            old_name='user',
            new_name='messager',
        ),
    ]
