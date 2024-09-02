import cv2
from cvzone.PoseModule import PoseDetector
from twilio.rest import Client
import time

detector = PoseDetector()
cap = cv2.VideoCapture(0)

# Set frame width and height
cap.set(3, 640)
cap.set(4, 480)
l = []

# Twilio credentials
account_sid = 'AC8e6e948d69f4054f3bc93987a0b52fca'
auth_token = '4c4e25bc4243c0fb620c5cd3bd6c4cf2'
twilio_client = Client(account_sid, auth_token)

def send_sms():
    message = twilio_client.messages.create(
        from_='+17178975175',
        body='Alert: Someone found!',
        to='+918864854298'
    )
    print(message.sid)

start_time = 0

while True:
    success, image = cap.read()

    if not success:
        print("Error: Failed to capture image from webcam.")
        break

    image = detector.findPose(image)
    imlist, bbox = detector.findPosition(image)

    cv2.imshow("RESULT", image)

    if image is None:
        continue

    elif len(imlist) > 0:
        l.append(1)
        if not start_time:
            start_time = time.time()

    elif len(l) > 30:
        if start_time and time.time() - start_time > 30:
            print("Someone is there!")
            send_sms()
            start_time = 0  # Reset the timer after sending the alert
            l = []  # Reset the counter after sending the alert

    # Press 'q' to exit the loop and close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
