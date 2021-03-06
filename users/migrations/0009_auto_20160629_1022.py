# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20160628_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='mobileNumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='postalCode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='birthDay',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='birthID',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='birthMonth',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='birthYear',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='familyName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='fatherName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='gender',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='nationalID',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
