import cv2
from twilio.rest import Client
import time

# Set up Twilio client with your credentials
account_sid = 'AC8e6e948d69f4054f3bc93987a0b52fca'
auth_token = '4c4e25bc4243c0fb620c5cd3bd6c4cf2'
client = Client(account_sid, auth_token)

# Initialize the camera using OpenCV
cap = cv2.VideoCapture(0)

# Load the OpenCV human body classifier
body_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

while True:
    # Capture frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect human bodies using the OpenCV human body classifier
    bodies = body_classifier.detectMultiScale(gray, 1.3, 5)

    # If a human body is detected, send an SMS alert using Twilio
    if len(bodies) > 0:
        for (x, y, w, h) in bodies:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        message = "Human body detected!"
        client.messages.create(
            to='+17178975175',  # replace with your recipient's phone number
            from_='+918864854298',  # replace with your Twilio phone number
            body=message
        )

    # Display the frame
    cv2.imshow('frame', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Delay before releasing the camera and destroying all windows
time.sleep(5)  # Add a delay of 5 seconds (you can adjust this as needed)
cap.release()
cv2.destroyAllWindows()
