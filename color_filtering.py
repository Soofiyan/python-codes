'''import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_yellow = np.uint8([[[0,0,0]]])
    lower_yellow = cv2.cvtColor(lower_yellow ,cv2.COLOR_BGR2HSV)

    upper_yellow = np.uint8([[[255,255,255]]])
    upper_yellow = cv2.cvtColor(upper_yellow ,cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
'''

# Python program for Detection of a
# specific color(blue here) using OpenCV with Python
import cv2
import numpy as np

# Webcamera no 0 is used to capture the frames
cap = cv2.VideoCapture(0)

# This drives the program into an infinite loop.
while (1):
    # Captures the live stream frame-by-frame
    _, frame = cap.read()
    # Converts images from BGR to HSV
    hsv = frame
    lower_red = np.array([0, 0, 0])
    upper_red = np.array([255, 255, 255])

    # Here we are defining range of bluecolor in HSV
    # This creates a mask of blue coloured
    # objects found in the frame.
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # The bitwise and of the frame and mask is done so
    # that only the blue coloured objects are highlighted
    # and stored in res
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    # This displays the frame, mask
    # and res which we created in 3 separate windows.
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# Destroys all of the HighGUI windows.
cv2.destroyAllWindows()

# release the captured frame
cap.release()