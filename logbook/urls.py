from . import views
from django.urls import path

urlpatterns = [
    path('', views.logbook_view, name='open_log'),

]