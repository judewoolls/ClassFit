from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Event
from django.views import generic

# Create your views here.
class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=0)
    template_name = 'booking/index.html'

def event_detail(request, id):
    queryset = Event.objects.filter(status=0)
    event = get_object_or_404(queryset, id=id)

    return render(
        request,
        "booking/event_detail.html",
        {"event": event}
    )