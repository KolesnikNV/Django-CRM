# Generated by Django 2.1.7 on 2019-06-03 13:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("invoices", "0003_auto_20190527_1620"),
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
                    ("Cancelled", "Cancel"),
                ],
                default="Draft",
                max_length=15,
            ),
        ),
    ]
