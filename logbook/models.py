from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = models.PositiveIntegerField()
    weight = models.FloatField()  # Use a decimal field if precision is critical
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.exercise.name} - {self.reps} reps @ {self.weight} kg"
