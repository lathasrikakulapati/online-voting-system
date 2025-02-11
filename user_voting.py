# voting/views.py
from django.shortcuts import render
from .models import Election, Vote
from django.contrib.auth.decorators import login_required

@login_required
def vote(request):
    if request.method == 'POST':
        election_id = request.POST['election_id']
        choice = request.POST['choice']

        # Get the current voter
        voter = Voter.objects.get(user=request.user)
        election = Election.objects.get(id=election_id)

        # Store the vote in the database
        vote = Vote(voter=voter, election=election, choice=choice)
        vote.save()

        return render(request, 'vote_success.html')

    elections = Election.objects.all()
    return render(request, 'vote.html', {'elections': elections})
