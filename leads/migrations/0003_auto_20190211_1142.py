# Generated by Django 2.1.5 on 2019-02-11 06:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("leads", "0002_lead_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lead",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
