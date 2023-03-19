# Generated by Django 3.2 on 2021-04-20 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210420_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='Category',
            field=models.CharField(choices=[('Luxury Suite', 'Luxury Suite'), ('Premier Suite', 'Premier Suite'), ('Deluxe Suite', 'Deluxe Suite')], max_length=15),
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]