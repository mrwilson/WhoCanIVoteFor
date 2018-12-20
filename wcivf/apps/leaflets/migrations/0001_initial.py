# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-24 15:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [("people", "0019_associatedcompany")]

    operations = [
        migrations.CreateModel(
            name="Leaflet",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("leaflet_id", models.IntegerField()),
                ("thumb_url", models.URLField(blank=True, null=True)),
                (
                    "date_uploaded_to_electionleaflets",
                    models.DateTimeField(blank=True, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="people.Person"
                    ),
                ),
            ],
        )
    ]
