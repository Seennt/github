# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-27 20:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0004_auto_20170627_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('explanation', models.TextField(null=True)),
                ('edited', models.DateField(auto_now_add=True)),
                ('filed', models.DateField(null=True)),
                ('completed', models.BooleanField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='actiondetails',
            name='action',
        ),
        migrations.RemoveField(
            model_name='action',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='action',
            name='filed',
        ),
        migrations.DeleteModel(
            name='ActionDetails',
        ),
        migrations.AddField(
            model_name='action',
            name='detail',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='todo_list.Detail'),
            preserve_default=False,
        ),
    ]