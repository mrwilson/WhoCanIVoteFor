# Generated by Django 2.2.7 on 2019-12-13 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("people", "0034_auto_20191213_0942")]

    operations = [
        migrations.AddField(
            model_name="personpost",
            name="votes_cast",
            field=models.PositiveSmallIntegerField(null=True),
        )
    ]