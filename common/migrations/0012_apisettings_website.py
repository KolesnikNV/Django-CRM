# Generated by Django 2.1.7 on 2019-02-19 10:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0011_auto_20190218_1230"),
    ]

    operations = [
        migrations.AddField(
            model_name="apisettings",
            name="website",
            field=models.URLField(default="", max_length=255),
        ),
    ]
