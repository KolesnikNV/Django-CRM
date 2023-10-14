# Generated by Django 2.1.7 on 2019-04-30 08:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0003_merge_20190214_1427"),
        ("accounts", "0006_auto_20190212_1708"),
    ]

    operations = [
        migrations.CreateModel(
            name="Email",
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
                ("sent_at", models.DateTimeField(auto_now_add=True)),
                ("message_subject", models.TextField(null=True)),
                ("message_body", models.TextField(null=True)),
                (
                    "recipient",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="recieved_email",
                        to="contacts.Contact",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="sent_email",
                        to="accounts.Account",
                    ),
                ),
            ],
        ),
    ]
