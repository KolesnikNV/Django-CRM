# Generated by Django 2.1.5 on 2019-02-12 08:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contact",
            options={"ordering": ["-created_on"]},
        ),
        migrations.RemoveField(
            model_name="contact",
            name="account",
        ),
        migrations.RemoveField(
            model_name="contact",
            name="teams",
        ),
        migrations.AlterField(
            model_name="contact",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="contact_created_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
