# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phoneNumber',
            field=models.IntegerField(blank=True, null='True'),
        ),
    ]