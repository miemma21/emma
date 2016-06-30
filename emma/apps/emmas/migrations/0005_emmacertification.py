# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-30 06:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emmas', '0004_emmastudies'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmmaCertification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certification', models.CharField(max_length=100, verbose_name='Certification')),
                ('time', models.CharField(max_length=100, verbose_name='Time')),
                ('emma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emmas.Emma', verbose_name='Emma')),
            ],
            options={
                'verbose_name': 'Emma Certification',
                'verbose_name_plural': 'Emma Certifications',
            },
        ),
    ]
