# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("elections", "0001_initial")]

    operations = [
        migrations.AlterModelOptions(
            name="election", options={"ordering": ["election_date"]}
        ),
        migrations.AddField(
            model_name="election",
            name="ballot_colour",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
