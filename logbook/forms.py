from django import forms
from .models import Exercise

class LeaderboardFilterForm(forms.Form):
    exercise = forms.ModelChoiceField(
        queryset=Exercise.objects.all(),
        required=False,
        label="Exercise",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    min_reps = forms.IntegerField(
        required=False,
        label="Min Reps",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 1})
    )
    min_weight = forms.FloatField(
        required=False,
        label="Min Weight (kg)",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 0})
    )