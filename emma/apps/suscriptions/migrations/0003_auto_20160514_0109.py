# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-14 06:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suscriptions', '0002_auto_20160513_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charge',
            name='amount',
            field=models.FloatField(max_length=100000, verbose_name='Amount'),
        ),
        migrations.AlterField(
            model_name='charge',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='charge',
            name='descripcion',
            field=models.TextField(max_length=30, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='charge',
            name='status',
            field=models.CharField(max_length=25, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='charge',
            name='suscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='charges', to='suscriptions.Suscription', verbose_name='Suscription'),
        ),
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='history',
            name='movement',
            field=models.CharField(max_length=200, verbose_name='Movement'),
        ),
        migrations.AlterField(
            model_name='history',
            name='suscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movements', to='suscriptions.Suscription', verbose_name='Suscription'),
        ),
    ]
