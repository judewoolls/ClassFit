from . import views
from django.urls import path

urlpatterns = [
    path('booking/', views.EventList.as_view(), name='booking'),
    path('<int:id>/', views.event_detail, name='event_detail'),
]