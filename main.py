import cv2
import time

video = cv2.VideoCapture(0)

# sleep for 1sec to let the camera load
time.sleep(1)

first_frame = None
while True:
    check, frame = video.read()

    # convert frame into gray_sframe and blur them
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (25, 25), 0)

    # caught first frame here
    if first_frame is None:
        first_frame = gray_frame_gau

    cv2.imshow("Video", frame)

    key = cv2.waitKey(0)
    if key == ord("s"):
        break

video.release()
