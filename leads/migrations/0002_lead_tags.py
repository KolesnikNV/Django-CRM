# Generated by Django 2.1.5 on 2019-02-01 13:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_auto_20190201_1840"),
        ("leads", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="lead",
            name="tags",
            field=models.ManyToManyField(blank=True, to="accounts.Tags"),
        ),
    ]
