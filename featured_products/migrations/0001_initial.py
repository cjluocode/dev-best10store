# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-20 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=500)),
                ('rating', models.FloatField()),
                ('rating_count', models.IntegerField()),
                ('hotscore', models.IntegerField()),
                ('image', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
