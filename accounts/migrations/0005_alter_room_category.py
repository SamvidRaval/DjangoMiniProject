# Generated by Django 3.2 on 2021-04-20 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210420_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='Category',
            field=models.CharField(choices=[('Luxury Suite', 'Luxury Suite'), ('Premier Suite', 'Premier Suite'), ('Deluxe Suite', 'Deluxe Suite')], max_length=15),
        ),
    ]
