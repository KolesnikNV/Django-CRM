# Generated by Django 3.0.6 on 2020-06-09 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0021_document_company"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="common.Company",
            ),
        ),
    ]
