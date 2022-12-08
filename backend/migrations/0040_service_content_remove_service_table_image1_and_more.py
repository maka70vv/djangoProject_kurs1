# Generated by Django 4.1.2 on 2022-11-28 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0039_service_table_delete_service_content"),
    ]

    operations = [
        migrations.CreateModel(
            name="Service_content",
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
                ("image1", models.ImageField(null=True, upload_to="")),
                ("image2", models.ImageField(null=True, upload_to="")),
                ("text_content", models.TextField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="service_table",
            name="image1",
        ),
        migrations.RemoveField(
            model_name="service_table",
            name="image2",
        ),
        migrations.RemoveField(
            model_name="service_table",
            name="text_content",
        ),
    ]