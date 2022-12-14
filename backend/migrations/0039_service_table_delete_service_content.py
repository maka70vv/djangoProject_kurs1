# Generated by Django 4.1.2 on 2022-11-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0038_remove_form_created_date_form_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Service_table",
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
                ("repair1", models.CharField(max_length=100)),
                ("repair2", models.CharField(max_length=100)),
                ("price1", models.CharField(max_length=20)),
                ("price2", models.CharField(max_length=20)),
                ("image1", models.ImageField(null=True, upload_to="")),
                ("image2", models.ImageField(null=True, upload_to="")),
                ("text_content", models.TextField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Service_content",
        ),
    ]
