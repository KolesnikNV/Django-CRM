# Generated by Django 3.2.7 on 2021-10-06 07:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0037_alter_profile_org"),
        ("cases", "0009_rename_company_case_org"),
    ]

    operations = [
        migrations.AlterField(
            model_name="case",
            name="org",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="case_org",
                to="common.org",
            ),
        ),
    ]
