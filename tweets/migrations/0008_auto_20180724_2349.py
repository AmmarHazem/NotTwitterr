# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-24 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0007_tweet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
