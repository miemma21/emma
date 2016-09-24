# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-24 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('amount', models.FloatField(max_length=100000, verbose_name='Amount')),
                ('status', models.CharField(choices=[(b'paid', b'Paid'), (b'pending', b'Pending')], max_length=25, verbose_name='Status')),
                ('card', models.CharField(max_length=25, verbose_name='Card')),
                ('file', models.FileField(upload_to=b'reports', verbose_name='File')),
            ],
            options={
                'verbose_name': 'Charge',
                'verbose_name_plural': 'Charges',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Creation date')),
                ('comments', models.TextField(verbose_name='Comments')),
                ('file', models.FileField(blank=True, null=True, upload_to=b'reports', verbose_name='File')),
            ],
            options={
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
            },
        ),
    ]
