# Generated by Django 3.2.5 on 2021-07-30 08:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0029_auto_20210730_1328"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("ADMIN", "ADMIN"), ("USER", "USER")], max_length=50
            ),
        ),
    ]
