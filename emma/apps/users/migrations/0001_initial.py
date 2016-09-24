# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-24 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoolUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email address')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('mother_last_name', models.CharField(max_length=30, verbose_name='Mother last name')),
                ('father_last_name', models.CharField(max_length=30, verbose_name='Father last name')),
                ('user_type', models.CharField(choices=[(b'emma', b'Emma'), (b'client', b'Client')], default=b'client', max_length=20, verbose_name='User type')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('join_date', models.DateField(auto_now_add=True, verbose_name='Join Date')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
