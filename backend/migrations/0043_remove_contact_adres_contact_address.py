# Generated by Django 4.1.2 on 2022-12-04 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0042_guides_text"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="adres",
        ),
        migrations.AddField(
            model_name="contact",
            name="address",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
