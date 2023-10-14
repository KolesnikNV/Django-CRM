# Generated by Django 2.2.10 on 2020-04-23 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0020_auto_20200409_1653"),
        ("contacts", "0004_contact_teams"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="common.Company",
            ),
        ),
    ]
