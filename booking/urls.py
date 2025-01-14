from . import views
from django.urls import path

urlpatterns = [
    path('booking/', views.EventList.as_view(), name='booking'),
]