# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-17 22:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='listy',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='list.List'),
        ),
    ]