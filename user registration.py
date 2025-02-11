# voting/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User model for registration
class Voter(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    voter_id = models.CharField(max_length=100, unique=True)
    face_encoding = models.BinaryField()  # Store the face encoding

    def __str__(self):
        return self.user.username

class Election(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name

class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.voter} voted for {self.choice}"
