# Generated by Django 3.2 on 2021-04-20 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20210420_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='Category',
            field=models.CharField(choices=[('Luxury Suite', 'Luxury Suite'), ('Deluxe Suite', 'Deluxe Suite'), ('Premier Suite', 'Premier Suite')], max_length=15),
        ),
    ]