# Generated by Django 3.1.7 on 2021-03-23 12:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0011_account_company"),
        ("cases", "0005_case_company"),
    ]

    operations = [
        migrations.AlterField(
            model_name="case",
            name="account",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="accounts_cases",
                to="accounts.account",
            ),
        ),
    ]
