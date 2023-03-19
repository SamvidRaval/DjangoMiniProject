from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class AvailabilityForm(forms.Form):
#     Room_Categories = {
#         ('Luxury Suite', 'Luxury Suite'),
#         ('Deluxe Suite', 'Deluxe Suite'),
#         ('Premier Suite', 'Premier Suite')
#     }
#     room_category = forms.ChoiceField(choices=Room_Categories, required=True)
#     Check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
#     Check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
