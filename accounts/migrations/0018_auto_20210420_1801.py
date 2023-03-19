# Generated by Django 3.2 on 2021-04-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_room_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='room',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='guest',
            name='user',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='room',
            name='Category',
            field=models.CharField(choices=[('Deluxe Suite', 'Deluxe Suite'), ('Premier Suite', 'Premier Suite'), ('Luxury Suite', 'Luxury Suite')], max_length=15),
        ),
    ]