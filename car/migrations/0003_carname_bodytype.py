# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-07 16:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_carname_fueltype'),
    ]

    operations = [
        migrations.AddField(
            model_name='carname',
            name='bodytype',
            field=models.CharField(default=datetime.datetime(2016, 9, 7, 16, 33, 13, 902193, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
    ]
