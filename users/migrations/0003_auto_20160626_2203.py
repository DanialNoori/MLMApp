# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 18:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160626_1022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appuser',
            options={'verbose_name': 'MLM User', 'verbose_name_plural': 'MLM Users'},
        ),
    ]