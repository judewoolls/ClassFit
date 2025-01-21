from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Event
from django.views import generic
from datetime import timedelta, datetime

# Create your views here.
class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=0)
    template_name = 'booking/booking_home.html'

def event_detail(request, id, date):
    current_date = datetime.strptime(date, "%Y-%m-%d").date()
    queryset = Event.objects.filter(status=0, date_of_event=current_date)
    event = get_object_or_404(queryset, id=id, date_of_event=current_date)

    return render(
        request,
        "booking/event_detail.html",
        {"event": event}
    )

def get_events_for_date(date):
    return Event.objects.filter(date_of_event=date).order_by('start_time')

def event_search(request, date):
    # Convert the string date to a datetime object
    current_date = datetime.strptime(date, "%Y-%m-%d").date()
    previous_date = current_date - timedelta(days=1)
    next_date = current_date + timedelta(days=1)

    # Query events for the current date
    events = Event.objects.filter(date_of_event=current_date, status=0)
    for event in events:
        event.is_user_booked = event.is_user_booked(request.user)

    return render(request, "booking/index.html", {
        "events": events,
        "current_date": current_date,
        "previous_date": previous_date,
        "next_date": next_date,
    })
