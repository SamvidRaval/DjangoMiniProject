# Generated by Django 3.2 on 2021-05-01 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_alter_room_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='Category',
            field=models.CharField(choices=[('Deluxe Suite', 'Deluxe Suite'), ('Luxury Suite', 'Luxury Suite'), ('Premier Suite', 'Premier Suite')], max_length=15),
        ),
    ]
