# Generated by Django 4.1.1 on 2023-10-07 12:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cms", "0005_blogcategory_blogdetailpage_show_legend_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="sitesettings",
            name="address",
            field=models.CharField(
                blank=True, help_text="address", max_length=250, null=True
            ),
        ),
        migrations.AddField(
            model_name="sitesettings",
            name="email",
            field=models.EmailField(
                blank=True, help_text="email", max_length=250, null=True
            ),
        ),
        migrations.AddField(
            model_name="sitesettings",
            name="phone",
            field=models.CharField(
                blank=True, help_text="phone", max_length=250, null=True
            ),
        ),
    ]
