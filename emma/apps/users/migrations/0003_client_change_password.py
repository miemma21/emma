# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 02:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160501_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='change_password',
            field=models.BooleanField(default=False),
        ),
    ]