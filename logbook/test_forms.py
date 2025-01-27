from django.test import TestCase
from django.contrib.auth.models import User
from logbook.models import Exercise, Score
from logbook.forms import ScoreForm

class ScoreFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpass')
        self.exercise = Exercise.objects.create(name='Test Exercise')

    def test_score_form_valid(self):
        form_data = {
            'exercise': self.exercise.id,
            'reps': 10,
            'weight': 50.0,
        }
        form = ScoreForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_score_form_invalid_missing_fields(self):
        form_data = {
            'exercise': self.exercise.id,
            'reps': 10,
            'weight': '',
        }
        form = ScoreForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_score_form_invalid_weight(self):
        form_data = {
            'exercise': self.exercise.id,  # Valid exercise
            'reps': 1,  # valid reps
            'weight': -10.0,  # Invalid weight
        }
        form = ScoreForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertNotIn('reps', form.errors)
        self.assertIn('weight', form.errors)

    def test_score_form_invalid_reps(self):
        form_data = {
            'exercise': self.exercise.id,  # Valid exercise
            'reps': -1,  # Invalid reps
            'weight': 10.0,  # Valid weight
        }
        form = ScoreForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertNotIn('weight', form.errors)
        self.assertIn('reps', form.errors)
