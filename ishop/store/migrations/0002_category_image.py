# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-11-21 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, default='placeholder.png', upload_to='images'),
        ),
    ]