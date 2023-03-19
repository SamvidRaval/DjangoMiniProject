from django.db import models


# Create your models here.
class Room(models.Model):
    Objects = None
    objects = None
    Room_Categories = {
        ('Luxury Suite', 'Luxury Suite'),
        ('Deluxe Suite', 'Deluxe Suite'),
        ('Premier Suite', 'Premier Suite')
    }
    Room_Number = models.IntegerField()
    Category = models.CharField(max_length=15, choices=Room_Categories)
    Guest_perRoom = models.IntegerField()

    def __str__(self):
        return f'{self.Room_Number}     {self.Category}     {self.Guest_perRoom} '


class Guest(models.Model):
    objects = None
    user = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=25)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=15)
    room = models.CharField(max_length=25)
    Check_in = models.DateTimeField()
    Check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user}    {self.email}    {self.phone}    {self.address}    {self.city}    {self.state}    {self.room}    {self.Check_in}    {self.Check_out}'


# class Contact_us(models.Model):
#     objects = None
#     user = models.CharField(max_length=15)
#     email = models.EmailField(max_length=20)
#     phone = models.CharField(max_length=10)
#
#     def __str__(self):
#         return f'{self.user}    {self.email}    {self.phone}'
