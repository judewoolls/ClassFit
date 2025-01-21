from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Event, Booking
from django.views import generic
from datetime import timedelta, datetime
from django.contrib import messages

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
    try:
        current_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return HttpResponse("Invalid date format", status=400)

    previous_date = current_date - timedelta(days=1)
    next_date = current_date + timedelta(days=1)

    events = Event.objects.filter(date_of_event=current_date, status=0)
    for event in events:
        event.is_user_booked = event.is_user_booked(request.user)

    return render(request, "booking/index.html", {
        "events": events,
        "current_date": current_date,
        "previous_date": previous_date,
        "next_date": next_date,
    })

def book_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        if event.is_full():
            messages.error(request, "Event is full")
            return redirect('event_search', date=event.date_of_event)

        if event.is_user_booked(request.user):
            messages.error(request, "You have already booked this event")
            return redirect('event_search', date=event.date_of_event)

        booking = Booking(event=event, user=request.user)
        booking.save()
        messages.success(request, "Event booked successfully")
        return redirect('event_search', date=event.date_of_event)
    return redirect('event_search', date=event.date_of_event)

def cancel_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        booking = Booking.objects.filter(event=event, user=request.user).first()
        if booking:
            booking.delete()
            messages.success(request, "Booking canceled successfully")
        else:
            messages.error(request, "You do not have a booking for this event")
        return redirect('event_search', date=event.date_of_event)
    return redirect('event_search', date=event.date_of_event)