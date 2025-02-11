# voting/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_voter, name='register'),
    path('login/', views.login_voter, name='login'),
    path('vote/', views.vote, name='vote'),
]
# online_voting_system/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('voting/', include('voting.urls')),  # Include voting app URLs
]
