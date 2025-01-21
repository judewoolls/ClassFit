from django.shortcuts import render

# Create your views here.
def logbook_view(request):
    return render(request, 'logbook/logbook.html')