# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_addr',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
    ]
