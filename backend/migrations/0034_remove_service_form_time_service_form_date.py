# Generated by Django 4.1.2 on 2022-11-22 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0033_service_form_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="service_form",
            name="time",
        ),
        migrations.AddField(
            model_name="service_form",
            name="date",
            field=models.DateTimeField(null=True),
        ),
    ]
