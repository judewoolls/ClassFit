from django.shortcuts import render, redirect
from .models import Exercise, Score
from .forms import LeaderboardFilterForm, ScoreForm

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
            

    if request.method == 'GET':
        leaderboard_filter = LeaderboardFilterForm(request.GET)
        if leaderboard_filter.is_valid():
            exercise = leaderboard_filter.cleaned_data.get('exercise')
            min_reps = leaderboard_filter.cleaned_data.get('min_reps')
            min_weight = leaderboard_filter.cleaned_data.get('min_weight')

            leaderboard = Score.objects.all()
            if exercise:
                leaderboard = leaderboard.filter(exercise=exercise)
            if min_reps:
                leaderboard = leaderboard.filter(reps__gte=min_reps)
            if min_weight:
                leaderboard = leaderboard.filter(weight__gte=min_weight)
        else:
            leaderboard = Score.objects.all()
    else:
        leaderboard_filter = LeaderboardFilterForm()
        leaderboard = Score.objects.all()

    return render(request, 'logbook/logbook.html', {
        'exercises': Exercise.objects.all(),
        'scores': scores,
        'filter': leaderboard_filter,
        'leaderboard': leaderboard.order_by('-weight', '-reps'),
        'scoreform': scoreform
    })