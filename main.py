import cv2
import time

video = cv2.VideoCapture(0)

# sleep for 1sec to let the camera load
time.sleep(1)

while True:
    check, frame = video.read()
    cv2.imshow("Video", frame)

    key = cv2.waitKey(0)
    if key == ord("s"):
        break

video.release()
