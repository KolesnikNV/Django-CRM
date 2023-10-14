# Generated by Django 4.1.1 on 2023-10-05 16:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0007_rename_company_event_org"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="event_type",
            field=models.CharField(
                choices=[
                    ("Recurring", "Recurring"),
                    ("Non-Recurring", "Non-Recurring"),
                    ("Call", "Call"),
                    ("Meeting", "Meeting"),
                    ("Task", "Task"),
                ],
                max_length=20,
            ),
        ),
    ]