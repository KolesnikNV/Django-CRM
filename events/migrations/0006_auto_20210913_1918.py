# Generated by Django 3.2 on 2021-09-13 13:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0034_auto_20210913_1918"),
        ("events", "0005_remove_event_company"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="common.company",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="assigned_to",
            field=models.ManyToManyField(
                blank=True, related_name="event_assigned", to="common.Profile"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="event_created_by_user",
                to="common.profile",
            ),
        ),
    ]
