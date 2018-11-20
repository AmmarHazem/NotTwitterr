# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-01 00:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_auto_20180629_2326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Retweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.CharField(max_length=256),
        ),
        migrations.AddField(
            model_name='retweet',
            name='tweet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tweets.Tweet'),
        ),
    ]
