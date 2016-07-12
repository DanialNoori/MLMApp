# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20160629_1428'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Adresses'},
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='address',
            name='mobileNumber',
            field=models.IntegerField(blank=True, null=True, verbose_name='Mobile Number'),
        ),
        migrations.AlterField(
            model_name='address',
            name='postalCode',
            field=models.IntegerField(blank=True, null=True, verbose_name='Postal Code'),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='birthDay',
            field=models.IntegerField(blank=True, null=True, verbose_name='Birth Day'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='birthID',
            field=models.IntegerField(blank=True, null=True, verbose_name='Birth Certificate ID'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='birthMonth',
            field=models.IntegerField(blank=True, null=True, verbose_name='Birth Month'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='birthYear',
            field=models.IntegerField(blank=True, null=True, verbose_name='Birth Year'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='emailValidated',
            field=models.BooleanField(default=False, verbose_name='Is Email Validated?'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='familyName',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Family Name'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='fatherName',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Father Name'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female')], max_length=1, null=True, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='mailToken',
            field=models.CharField(blank=True, max_length=20, verbose_name='Email Token'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='nationalID',
            field=models.IntegerField(blank=True, null=True, verbose_name='National ID'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='profilePicture',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/', verbose_name='Avatar'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='validated',
            field=models.BooleanField(default=False, verbose_name='Is Mobile Phone Validated?'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='validationCode',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Validation Code'),
        ),
        migrations.AlterField(
            model_name='parenthood',
            name='validatedByParent',
            field=models.CharField(choices=[('accepted', 'Accepted'), ('pending', 'Pending'), ('denied', 'Denied')], default='pending', max_length=10, verbose_name='Has Upline Validated?'),
        ),
    ]