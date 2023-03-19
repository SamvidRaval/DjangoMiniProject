# Generated by Django 3.2 on 2021-05-16 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_auto_20210516_0944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_us',
            old_name='guestname',
            new_name='user2',
        ),
        migrations.AlterField(
            model_name='room',
            name='Category',
            field=models.CharField(choices=[('Luxury Suite', 'Luxury Suite'), ('Deluxe Suite', 'Deluxe Suite'), ('Premier Suite', 'Premier Suite')], max_length=15),
        ),
    ]
