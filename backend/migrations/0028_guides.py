# Generated by Django 4.1.2 on 2022-11-21 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0027_service_content_service_form_delete_service"),
    ]

    operations = [
        migrations.CreateModel(
            name="Guides",
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
                ("video1", models.URLField()),
                ("video2", models.URLField()),
                ("video3", models.URLField()),
                ("video4", models.URLField()),
                ("image_down1", models.ImageField(upload_to="")),
                ("image_down2", models.ImageField(upload_to="")),
                ("image_down3", models.ImageField(upload_to="")),
            ],
        ),
    ]
