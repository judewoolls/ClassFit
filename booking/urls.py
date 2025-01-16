from . import views
from django.urls import path

urlpatterns = [
    path('<str:date>/', views.event_search, name='event_search'),
    path('<str:date>/<int:id>/', views.event_detail, name='event_detail'),
]