# Generated by Django 4.1.2 on 2022-11-19 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0022_delete_order"),
    ]

    operations = [
        migrations.CreateModel(
            name="Send",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
    ]
