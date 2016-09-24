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
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='HiredService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_days', models.TextField(verbose_name='Service Days')),
            ],
            options={
                'verbose_name': 'Hired service',
                'verbose_name_plural': 'Hired services',
            },
        ),
        migrations.CreateModel(
            name='ScheduledCall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('date_time', models.CharField(max_length=20, verbose_name='Date and time')),
                ('number', models.BigIntegerField(verbose_name='Number')),
            ],
            options={
                'verbose_name': 'Scheduled call',
                'verbose_name_plural': 'Scheduled calls',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('max_weekly_sessions', models.IntegerField(blank=True, null=True)),
                ('weekly_hours', models.IntegerField(blank=True, null=True)),
                ('price', models.PositiveSmallIntegerField(verbose_name='Price')),
                ('allows_workshops', models.BooleanField(default=False, verbose_name='Allows workshops')),
                ('allows_activities', models.BooleanField(default=False, verbose_name='Allows activities')),
                ('max_hours_per_month', models.IntegerField(blank=True, null=True, verbose_name='Max hours per month')),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Plans',
            },
        ),
    ]
