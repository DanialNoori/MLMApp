# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20160702_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='associtedWithRole',
            field=models.CharField(blank=True, choices=[('q', 'qualify'), ('b', 'bronze'), ('silver', 'silver'), ('g', 'gold'), ('p', 'platinium')], max_length=10, null=True),
        ),
    ]
