from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, 'Active'),(1,'Expired'))
EVENT_STATUS = ((0, 'Future'),(1,'Past'))

# Create your models here.

#### Event model ######

class Coach(models.Model):
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name="coach")
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.coach.username}"

class Event(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    coach = models.ForeignKey(
        Coach, on_delete=models.CASCADE, related_name="coach_on_booking"
    )
    event_name = models.CharField(max_length=200)
    description = models.TextField()
    date_of_event = models.DateField()
    capacity = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.IntegerField(choices=EVENT_STATUS)

    def number_of_bookings(self):
        return self.event_booking.count() 
    
    def is_full(self):
        return self.number_of_bookings() >= self.capacity

    def is_user_booked(self, user):
        return self.event_booking.filter(user=user).exists()

    def __str__(self):
        return f"{self.event_name}: {self.date_of_event} from {self.start_time} to {self.end_time}"  
    
#### Booking model ######

class Booking(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="event_booking"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_booking"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"{STATUS[self.status][1]} Booking #{self.id} for {self.event.event_name} by {self.user.username}"

    class Meta:
        ordering = ["status"]
