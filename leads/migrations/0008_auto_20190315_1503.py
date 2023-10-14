# Generated by Django 2.1.7 on 2019-03-15 09:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("leads", "0007_auto_20190306_1226"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lead",
            name="first_name",
            field=models.CharField(
                max_length=255, null=True, verbose_name="First name"
            ),
        ),
        migrations.AlterField(
            model_name="lead",
            name="last_name",
            field=models.CharField(max_length=255, null=True, verbose_name="Last name"),
        ),
        migrations.AlterField(
            model_name="lead",
            name="title",
            field=models.CharField(
                default="title", max_length=64, verbose_name="Title"
            ),
            preserve_default=False,
        ),
    ]
