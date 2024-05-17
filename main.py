import cv2
import time
from Send_Email import send_email
import numpy

video = cv2.VideoCapture(0)

# sleep for 1sec to let the camera load
time.sleep(1)

first_frame = None
object_frame = None
main_status_list = []
while True:
    status = 0
    check, frame = video.read()

    # convert frame into gray_sframe and blur them
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (25, 25), 0)

    # caught first frame here
    if first_frame is None:
        first_frame = gray_frame_gau

    # diff first_frame and gray_frame_gau to detect object
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)

    # convert delta_frame to thresh_frame to Clear the disturbance in the delta_frame
    # thresh to convert object greater than 65 BGR to Max 255 BGR
    thresh_frame = cv2.threshold(delta_frame, 65, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # Find the Contours/sides-of-object to make it easier to draw rectangles
    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # for smaller values such as shadows, just continue the loop
        if cv2.contourArea(contour) < 5000:
            continue

        # get x-point and y-point and width and length of rectangle
        x, y, w, h = cv2.boundingRect(contour)
        # create Rectangle on frame
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        if rectangle.any():
            status = 1

        if object_frame is None:
            object_frame = frame
            frame = numpy.array(frame)
            cv2.imwrite("image.png", frame)

    main_status_list.append(status)
    status_list = main_status_list[-2:]
    if status_list[0] == 1 and status_list[1] == 0:
        send_email()

    cv2.imshow("Video", frame)

    # create break-loop Keyboard-key "s" to break the loop and stop camera
    key = cv2.waitKey(0)
    if key == ord("s"):
        break

video.release()
