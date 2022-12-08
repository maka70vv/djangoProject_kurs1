# Generated by Django 4.1.2 on 2022-11-14 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0016_rename_main_main_m"),
    ]

    operations = [
        migrations.CreateModel(
            name="Form",
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
                (
                    "title_broken",
                    models.CharField(
                        choices=[
                            ("TV", "TV"),
                            ("Refrigerator", "Refrigerator"),
                            ("Microwave ovens", "Microwave ovens"),
                            ("Washing machine", "Washing machine"),
                            ("Electric cooker", "Electric cooker"),
                            ("Gas cooker", "Gas cooker"),
                            ("Vacuum cleaner", "Vacuum cleaner"),
                            ("Irons", "Irons"),
                            ("Electric kettle", "Electric kettle"),
                        ],
                        max_length=100,
                    ),
                ),
                ("quatity_food", models.IntegerField(null=True)),
                ("name", models.CharField(max_length=100)),
                ("number_phone", models.CharField(max_length=13)),
                ("address", models.CharField(max_length=60)),
            ],
        ),
        migrations.RenameModel(
            old_name="Main_m",
            new_name="Main",
        ),
    ]
