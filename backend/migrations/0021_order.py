# Generated by Django 4.1.2 on 2022-11-17 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_delete_send'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_fast_food', models.CharField(choices=[('OAZIS', 'OAZIS'), ('BIR EKI', 'BIR EKI'), ('IMPERIA PIZZA', 'IMPERIA PIZZA'), ('EKIDOS', 'EKIDOS'), ('PAPAJOHNS', 'PAPAJOHNS'), ('DODOPIZZA', 'DODOPIZZA'), ('KFC', 'KFC')], max_length=100)),
                ('quatity_food', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=100)),
                ('number_phone', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=60)),
                ('choise_food', models.CharField(choices=[('HAMBURGER', 'HAMBURGER'), ('PIZZA', 'PIZZA'), ('CHICKEN ROLS', 'CHICKEN ROLS'), ('DONNER', 'DONNER'), ('RAMEN', 'RAMEN'), ('POTATOES FREE', 'POTATOES FREE'), ('SANDWITCH', 'SANDWITCH')], max_length=100)),
            ],
        ),
    ]
