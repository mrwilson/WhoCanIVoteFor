# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-18 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("people", "0014_auto_20170518_1009")]

    operations = [
        migrations.RemoveField(model_name="person", name="id"),
        migrations.AlterField(
            model_name="person",
            name="ynr_id",
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
