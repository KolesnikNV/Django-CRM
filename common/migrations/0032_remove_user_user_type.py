# Generated by Django 3.2.5 on 2021-08-20 06:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0031_auto_20210805_1214"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="user_type",
        ),
    ]
