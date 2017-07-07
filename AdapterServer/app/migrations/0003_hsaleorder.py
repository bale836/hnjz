# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-02 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170702_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='HSaleOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderID', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'h_s_order',
            },
        ),
    ]