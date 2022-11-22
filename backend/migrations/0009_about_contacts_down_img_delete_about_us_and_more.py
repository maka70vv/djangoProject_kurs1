# Generated by Django 4.1.2 on 2022-11-06 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_about_us_contact_delete_about_delete_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='')),
                ('image2', models.ImageField(upload_to='')),
                ('image3', models.ImageField(upload_to='')),
                ('partners', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=50, null=True)),
                ('name2', models.CharField(max_length=50, null=True)),
                ('name3', models.CharField(max_length=50, null=True)),
                ('insta', models.CharField(max_length=40, null=True)),
                ('phone_number1', models.CharField(max_length=15)),
                ('phone_number2', models.CharField(max_length=15)),
                ('phone_number3', models.CharField(max_length=15)),
                ('adres', models.CharField(max_length=100)),
                ('image_mem', models.ImageField(upload_to='')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Down_img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_down1', models.ImageField(upload_to='')),
                ('image_down2', models.ImageField(upload_to='')),
                ('image_down3', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='About_us',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
