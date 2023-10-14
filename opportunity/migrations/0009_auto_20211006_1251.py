# Generated by Django 3.2.7 on 2021-10-06 07:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0037_alter_profile_org"),
        ("opportunity", "0008_rename_company_opportunity_org"),
    ]

    operations = [
        migrations.AlterField(
            model_name="opportunity",
            name="closed_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="oppurtunity_closed_by",
                to="common.profile",
            ),
        ),
        migrations.AlterField(
            model_name="opportunity",
            name="org",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="oppurtunity_org",
                to="common.org",
            ),
        ),
    ]
