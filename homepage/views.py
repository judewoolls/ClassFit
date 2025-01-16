from django.shortcuts import render

## home page views
def home(request):
    return render(request, 'homepage/home.html')
