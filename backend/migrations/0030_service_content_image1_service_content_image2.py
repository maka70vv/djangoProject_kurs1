# Generated by Django 4.1.2 on 2022-11-21 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0029_service_content_image_down1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_content',
            name='image1',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='service_content',
            name='image2',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
