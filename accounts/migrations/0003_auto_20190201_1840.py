# Generated by Django 2.1.5 on 2019-02-01 13:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_auto_20190128_1237"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tags",
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
                ("name", models.CharField(max_length=20)),
                ("slug", models.CharField(blank=True, max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="account",
            name="tags",
            field=models.ManyToManyField(blank=True, to="accounts.Tags"),
        ),
    ]
