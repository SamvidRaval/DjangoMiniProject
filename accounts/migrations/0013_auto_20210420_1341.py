# Generated by Django 3.2 on 2021-04-20 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20210420_1159'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AlterField(
            model_name='room',
            name='Category',
            field=models.CharField(choices=[('Premier Suite', 'Premier Suite'), ('Deluxe Suite', 'Deluxe Suite'), ('Luxury Suite', 'Luxury Suite')], max_length=15),
        ),
    ]
