# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("elections", "0003_post")]

    operations = [
        migrations.CreateModel(
            name="VotingSystem",
            fields=[
                ("slug", models.SlugField(primary_key=True, serialize=False)),
                ("name", models.CharField(blank=True, max_length=100)),
                ("wikipedia_url", models.URLField(blank=True)),
                ("description", models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name="election",
            name="voting_system",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="elections.VotingSystem",
            ),
        ),
    ]
