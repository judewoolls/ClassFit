from django.shortcuts import render, redirect
from .models import Exercise, Score
from .forms import ScoreForm

# Create your views here.
def logbook_view(request):

    scores = Score.objects.filter(user=request.user).order_by('-created_on')
    scoreform = ScoreForm()

    if request.method == 'POST':
        scoreform = ScoreForm(request.POST)
        if scoreform.is_valid():
            score = scoreform.save(commit=False)
            score.user = request.user
            score.save()
            scoreform = ScoreForm()
            return redirect('open_log')
            

    return render(request, 'logbook/logbook.html', {
        'exercises': Exercise.objects.all(),
        'scores': scores,
        'scoreform': scoreform
    })