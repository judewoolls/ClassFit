from . import views
from django.urls import path

urlpatterns = [
    path('booking/', views.EventList.as_view(), name='booking'),
    path('booking/<str:date>/', views.event_search, name='event_search'),
    path('booking/<str:date>/<int:id>/', views.event_detail, name='event_detail'),
]