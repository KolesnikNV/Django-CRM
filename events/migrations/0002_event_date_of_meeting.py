# Generated by Django 2.1.7 on 2019-06-03 13:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="date_of_meeting",
            field=models.DateField(blank=True, null=True),
        ),
    ]
