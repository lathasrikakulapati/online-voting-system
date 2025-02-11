# voting/admin.py
from django.contrib import admin
from .models import Election, Vote, Voter

admin.site.register(Election)
admin.site.register(Vote)
admin.site.register(Voter)
