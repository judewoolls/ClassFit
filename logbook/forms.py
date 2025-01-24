from django import forms
from .models import Exercise, Score


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['exercise', 'reps', 'weight']
        widgets = {
            'exercise': forms.Select(attrs={'class': 'form-control'}),
            'reps': forms.NumberInput(attrs={'class': 'form-control',
                                             'min': 1}),
            'weight': forms.NumberInput(attrs={'class': 'form-control',
                                               'min': 0})
        }
