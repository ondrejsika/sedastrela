# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 20:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=32)),
                ('link', models.URLField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Menu')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Page')),
            ],
        ),
    ]