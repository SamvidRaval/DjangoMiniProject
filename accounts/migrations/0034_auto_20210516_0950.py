# Generated by Django 3.2 on 2021-05-16 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_auto_20210516_0949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_us',
            old_name='user2',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='room',
            name='Category',
            field=models.CharField(choices=[('Premier Suite', 'Premier Suite'), ('Luxury Suite', 'Luxury Suite'), ('Deluxe Suite', 'Deluxe Suite')], max_length=15),
        ),
    ]
