import cv2
from cvzone.PoseModule import PoseDetector
import send

detector = PoseDetector()
cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

while not cap.isOpened():
    print("Error: Failed to open the camera.")
    cv2.waitKey(1000)

print("Camera opened.")

while True:
    success, image = cap.read()

    if not success:
        print("Error: Failed to capture image from webcam.")
        break

    image = detector.findPose(image)
    bbox, _ = detector.findPosition(image)

    cv2.imshow("\t\tHUMAN POSE DETECTOR TOOL", image)

    if not bbox:
        print("No one detected!")
    else:
        print("human detected!")

    if cap.isOpened() and bbox:
         send.sendSms() 

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
