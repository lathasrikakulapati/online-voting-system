# voting/views.py
import face_recognition
import base64
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django_otp.decorators import otp_required
import json
import numpy as np
import cv2

@otp_required
def login_voter(request):
    if request.method == 'POST':
        # Extract base64 image data from request
        data = json.loads(request.body)
        image_data = data['image_data']
        image_data = image_data.split(',')[1]  # Remove the "data:image/jpeg;base64," part
        image_bytes = base64.b64decode(image_data)

        # Convert the image into a numpy array
        np_img = np.frombuffer(image_bytes, dtype=np.uint8)
        img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

        # Convert the image to RGB (for face_recognition)
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face_encodings = face_recognition.face_encodings(rgb_img)

        if face_encodings:
            # Match face encoding from webcam with the stored face encoding in the database
            captured_face_encoding = face_encodings[0]  # Assume one face detected
            voter = Voter.objects.get(user=request.user)
            match = face_recognition.compare_faces([voter.face_encoding], captured_face_encoding)

            if match[0]:
                # Face match successful, proceed to 2FA
                # Send OTP for 2FA (e.g., send an OTP via email or SMS)
                return JsonResponse({"success": True})
            else:
                return JsonResponse({"success": False})

    return render(request, 'login.html')
