# Generated by Django 3.2 on 2021-04-20 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_guest_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='Category',
            field=models.CharField(choices=[('Premier Suite', 'Premier Suite'), ('Luxury Suite', 'Luxury Suite'), ('Deluxe Suite', 'Deluxe Suite')], max_length=15),
        ),
    ]
