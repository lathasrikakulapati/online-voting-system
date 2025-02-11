# voting/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_voter, name='register'),
    path('login/', views.login_voter, name='login'),
    path('vote/', views.vote, name='vote'),
]
