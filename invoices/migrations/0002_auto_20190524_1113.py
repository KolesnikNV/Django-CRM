# Generated by Django 2.1.7 on 2019-05-24 05:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("invoices", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="status",
            field=models.CharField(
                choices=[
                    ("Draft", "Draft"),
                    ("Sent", "Sent"),
                    ("Paid", "Paid"),
                    ("Pending", "Pending"),
                    ("Cancel", "Cancel"),
                ],
                default="Draft",
                max_length=15,
            ),
        ),
    ]
