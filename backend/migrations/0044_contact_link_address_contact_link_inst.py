# Generated by Django 4.1.2 on 2022-12-04 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0043_remove_contact_adres_contact_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="link_address",
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name="contact",
            name="link_inst",
            field=models.URLField(null=True),
        ),
    ]
