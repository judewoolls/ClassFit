from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Event, Booking, Coach
from .forms import EventForm
from datetime import datetime, timedelta

class BookingViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.coach = Coach.objects.create(coach=self.user)
        self.event = Event.objects.create(
            coach=self.coach,
            event_name='Test Event',
            description='This is a test event.',
            date_of_event='2023-12-31',
            capacity=10,
            start_time='10:00',
            end_time='12:00',
            status=0,
        )

    def test_event_detail_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('event_detail', args=[self.event.date_of_event, self.event.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/event_detail.html')

    def test_event_search_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('event_search', args=['2023-12-31']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/index.html')

    def test_book_event_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('book_event', args=[self.event.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Booking.objects.filter(event=self.event, user=self.user).exists())

    def test_cancel_event_view(self):
        self.client.login(username='testuser', password='testpass')
        booking = Booking.objects.create(event=self.event, user=self.user)
        response = self.client.post(reverse('cancel_event', args=[self.event.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Booking.objects.filter(event=self.event, user=self.user).exists())

    def test_delete_event_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('delete_event', args=[self.event.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Event.objects.filter(id=self.event.id).exists())

    def test_create_event_view(self):
        self.client.login(username='testuser', password='testpass')
        form_data = {
            'coach': self.coach.id,
            'event_name': 'New Event',
            'description': 'This is a new event.',
            'date_of_event': '2023-12-31',
            'capacity': 10,
            'start_time': '14:00',
            'end_time': '16:00',
            'status': 0,
        }
        response = self.client.post(reverse('create_event'), data=form_data)
        self.assertEqual(response.status_code, 302, msg=f"Response content: {response.content}")
        self.assertTrue(Event.objects.filter(event_name='New Event').exists())

    def test_edit_event_view(self):
        self.client.login(username='testuser', password='testpass')
        form_data = {
            'coach': self.coach.id,
            'event_name': 'Updated Event',
            'description': 'This is an updated event.',
            'date_of_event': '2023-12-31',
            'capacity': 15,
            'start_time': '10:00',
            'end_time': '12:00',
            'status': 0,
        }
        response = self.client.post(reverse('edit_event', args=[self.event.id]), data=form_data)
        self.assertEqual(response.status_code, 302, msg=f"Response content: {response.content}")
        self.event.refresh_from_db()
        self.assertEqual(self.event.event_name, 'Updated Event', msg=f"Event name: {self.event.event_name}")
        self.assertEqual(self.event.capacity, 15, msg=f"Event capacity: {self.event.capacity}")