import datetime
from accounts.models import Room, Guest


def check_availability(room, check_in, check_out):
    avail_list = []
    booking_list = Guest.objects.filter(room=room)
    for booking in booking_list:
        if booking.check_in > check_out or booking.check_out < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)