from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from django.views import generic

# Create your views here.
class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=0)
    template_name = 'booking/index.html'