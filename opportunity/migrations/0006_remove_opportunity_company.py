# Generated by Django 3.1.7 on 2021-03-24 08:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("opportunity", "0005_opportunity_company"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="opportunity",
            name="company",
        ),
    ]
