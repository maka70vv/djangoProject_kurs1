# Generated by Django 4.1.2 on 2022-11-28 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0040_service_content_remove_service_table_image1_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Service_table",
        ),
        migrations.AddField(
            model_name="service_content",
            name="image_down1",
            field=models.ImageField(null=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="service_content",
            name="image_down2",
            field=models.ImageField(null=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="service_content",
            name="image_down3",
            field=models.ImageField(null=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="service_content",
            name="price1",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="service_content",
            name="price2",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="service_content",
            name="price3",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="service_content",
            name="price4",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="service_content",
            name="price5",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="service_content",
            name="price6",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="service_content",
            name="price7",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="service_content",
            name="price8",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="service_content",
            name="price9",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="service_content",
            name="repair1",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="service_content",
            name="repair2",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="service_content",
            name="repair3",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="service_content",
            name="repair4",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="service_content",
            name="repair5",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="service_content",
            name="repair6",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="service_content",
            name="repair7",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="service_content",
            name="repair8",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="service_content",
            name="repair9",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
