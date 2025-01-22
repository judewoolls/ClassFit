from django.shortcuts import render
from booking.models import Booking
from logbook.models import Score
from django.contrib.auth.models import User

# Home page view
def home(request):
    # Get the current user
    user = request.user

    # Query bookings made by the user and order by the date of the event
    bookings = Booking.objects.filter(user=user).order_by('event__date_of_event')
    #Query scores made by the user
    scores =  Score.objects.filter(user=user).order_by('-created_on')

    return render(request, 'homepage/home.html', {
        'bookings': bookings,
        'scores': scores
    })
