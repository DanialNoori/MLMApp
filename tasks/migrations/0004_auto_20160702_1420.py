# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 10:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_associtedwithrole'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='audioFile',
            field=models.FileField(blank=True, null=True, upload_to='audio_files/', verbose_name='Audio File'),
        ),
        migrations.AddField(
            model_name='task',
            name='examScore',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='scheduler',
            name='accepted',
            field=models.BooleanField(default=False, verbose_name='Accepted'),
        ),
        migrations.AlterField(
            model_name='scheduler',
            name='accomplished',
            field=models.BooleanField(default=False, verbose_name='Accomplished?'),
        ),
        migrations.AlterField(
            model_name='scheduler',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Task', verbose_name='Task'),
        ),
        migrations.AlterField(
            model_name='scheduler',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.AppUser', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='task',
            name='associtedWithRole',
            field=models.CharField(blank=True, choices=[('q', 'qualify'), ('b', 'bronze'), ('silver', 'silver'), ('g', 'gold'), ('p', 'platinium')], max_length=10, null=True, verbose_name='Associated With Role:'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.TextField(verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='task',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of Role:'),
        ),
    ]