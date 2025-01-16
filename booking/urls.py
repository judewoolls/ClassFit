from . import views
from django.urls import path

urlpatterns = [
    path('', views.EventList.as_view(), name='booking'),
    path('<str:date>/', views.event_search, name='event_search'),
    path('<str:date>/<int:id>/', views.event_detail, name='event_detail'),
]