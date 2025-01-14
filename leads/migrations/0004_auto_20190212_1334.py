# Generated by Django 2.1.5 on 2019-02-12 08:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0002_auto_20190212_1334"),
        ("leads", "0003_auto_20190211_1142"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="lead",
            name="account",
        ),
        migrations.RemoveField(
            model_name="lead",
            name="teams",
        ),
        migrations.AddField(
            model_name="lead",
            name="contacts",
            field=models.ManyToManyField(
                related_name="lead_contacts", to="contacts.Contact"
            ),
        ),
        migrations.AlterField(
            model_name="lead",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="lead_created_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
