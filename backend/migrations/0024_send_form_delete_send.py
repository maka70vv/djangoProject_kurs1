# Generated by Django 4.1.2 on 2022-11-19 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0023_send'),
    ]

    operations = [
        migrations.CreateModel(
            name='Send_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=13)),
                ('broken', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Send',
        ),
    ]
