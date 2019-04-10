import numpy as np
import cv2
import sys
import tkinter as tk
from tkinter import filedialog

while (1):
    def pick_color(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            pixel = image_hsv[y, x]

            # HUE, SATURATION, AND VALUE (BRIGHTNESS) RANGES. TOLERANCE COULD BE ADJUSTED.
            upper = np.array([pixel[0] + 10, pixel[1] + 10, pixel[2] + 40])
            lower = np.array([pixel[0] - 10, pixel[1] - 10, pixel[2] - 40])
            assert isinstance(upper, object)
            print(lower, upper)

            # A MONOCHROME MASK FOR GETTING A BETTER VISION OVER THE COLORS
            #image_mask = cv2.inRange(image_hsv, lower, upper)
            #cv2.imshow("Mask", image_mask)
        ret

    
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    # img = cv2.cvtColor(frame,0)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    horizontal_img = cv2.flip(frame, 1)
    # cv2.imshow('gray',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # OPEN DIALOG FOR READING THE IMAGE FILE
    root = tk.Tk()
    root.withdraw()  # HIDE THE TKINTER GUI
    cv2.imshow("BGR", horizontal_img)

    # CREATE THE HSV FROM THE BGR IMAGE

    image_hsv = cv2.cvtColor(horizontal_img, cv2.COLOR_BGR2HSV)

    # CALLBACK FUNCTION
    cv2.setMouseCallback("BGR",pick_color)

release = cap.release()
cv2.destroyAllWindows()

