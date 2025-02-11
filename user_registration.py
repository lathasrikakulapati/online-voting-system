# voting/views.py
import face_recognition
from django.shortcuts import render, redirect
from .models import Voter
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

def register_voter(request):
    if request.method == "POST":
        # Get form data (username, voter ID, image upload)
        username = request.POST['username']
        voter_id = request.POST['voter_id']
        image = request.FILES['image']  # Image file with the face

        # Load the image using face_recognition
        face_image = face_recognition.load_image_file(image)
        face_encoding = face_recognition.face_encodings(face_image)[0]

        # Create user and voter entry in the database
        user = User.objects.create_user(username=username, password=request.POST['password'])
        user.save()

        voter = Voter(user=user, voter_id=voter_id, face_encoding=face_encoding)
        voter.save()

        return redirect('login')  # Redirect to login page after registration
    
    return render(request, 'register.html')
