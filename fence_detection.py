import numpy as np
import cv2
import sys
import tkinter as tk
from tkinter import filedialog

global lower_value_r,lower_value_g,lower_value_b,upper_value_r,upper_value_g,upper_value_b

lower_r_low = np.uint8(255)
lower_g_low = np.uint8(255)
lower_b_low = np.uint8(255)
upper_r_low = np.uint8(0)
upper_g_low = np.uint8(0)
upper_b_low = np.uint8(0)

lower_h_low = np.uint8(255)
lower_s_low = np.uint8(255)
lower_v_low = np.uint8(255)
upper_h_low = np.uint8(0)
upper_s_low = np.uint8(0)
upper_v_low = np.uint8(0)

while (1):
    def pick_color(event, x, y, flags, param):
        global lower_r_low, lower_g_low, lower_b_low, upper_r_low, upper_g_low, upper_b_low
        global lower_h_low, lower_s_low, lower_v_low, upper_h_low, upper_s_low, upper_v_low
        if event == cv2.EVENT_LBUTTONDOWN:
            pixel_hsv = image_hsv[y, x]
            pixel_rgb = image_rgb[y, x]
            # HUE, SATURATION, AND VALUE (BRIGHTNESS) RANGES. TOLERANCE COULD BE ADJUSTED.
            pixel_hsv_low = np.array([pixel_hsv[0]-10, pixel_hsv[1]-10, pixel_hsv[2]-30])
            pixel_hsv_high = np.array([pixel_hsv[0]+10, pixel_hsv[1]+10, pixel_hsv[2]+30])

            pixel_rgb_low = np.array([pixel_rgb[0] - 10, pixel_rgb[1] - 10, pixel_rgb[2] - 30])
            pixel_rgb_high = np.array([pixel_rgb[0] + 10, pixel_rgb[1] + 10, pixel_rgb[2] + 30])
            #print(upper,lower)
            #print(np.uint8(lower), np.uint8(upper))
            #print(np.uint8(lower[0]),np.uint8(lower[1]),np.uint8(lower[2]))
            lower_value_h = np.uint8(pixel_hsv_low[0])
            lower_value_s = np.uint8(pixel_hsv_low[1])
            lower_value_v = np.uint8(pixel_hsv_low[2])
            upper_value_h = np.uint8(pixel_hsv_high[0])
            upper_value_s = np.uint8(pixel_hsv_high[1])
            upper_value_v = np.uint8(pixel_hsv_high[2])

            lower_value_r = np.uint8(pixel_rgb_low[0])
            lower_value_g = np.uint8(pixel_rgb_low[1])
            lower_value_b = np.uint8(pixel_rgb_low[2])
            upper_value_r = np.uint8(pixel_rgb_high[0])
            upper_value_g = np.uint8(pixel_rgb_high[1])
            upper_value_b = np.uint8(pixel_rgb_high[2])

            # A MONOCHROME MASK FOR GETTING A BETTER VISION OVER THE COLORS
            #image_mask = cv2.inRange(image_hsv, lower, upper)
            #cv2.imshow("Mask", image_mask)

            if lower_value_r < lower_r_low :
                lower_r_low = lower_value_r
            if lower_value_g < lower_g_low :
                lower_g_low = lower_value_g
            if lower_value_b < lower_b_low :
                lower_b_low = lower_value_b
            if upper_value_r > upper_r_low :
                upper_r_low = upper_value_r
            if upper_value_g > upper_g_low :
                upper_g_low = upper_value_g
            if upper_value_b > upper_b_low :
                upper_b_low = upper_value_b

            if lower_value_h < lower_h_low :
                lower_h_low = lower_value_h
            if lower_value_s < lower_s_low :
                lower_s_low = lower_value_s
            if lower_value_v < lower_v_low :
                lower_v_low = lower_value_v
            if upper_value_h > upper_h_low :
                upper_h_low = upper_value_h
            if upper_value_s > upper_s_low :
                upper_s_low = upper_value_s
            if upper_value_v > upper_v_low :
                upper_v_low = upper_value_v

            print(lower_r_low,lower_g_low,lower_b_low)
            print(upper_r_low,upper_g_low,upper_b_low)
            print(lower_h_low, lower_s_low, lower_v_low)
            print(upper_h_low, upper_s_low, upper_v_low)
            print("\n")

        ret
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    # img = cv2.cvtColor(frame,0)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    horizontal_img = cv2.flip(frame, 1)
    image_rgb = horizontal_img
    # cv2.imshow('gray',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # OPEN DIALOG FOR READING THE IMAGE FILE
    root = tk.Tk()
    root.withdraw()  # HIDE THE TKINTER GUI
    cv2.imshow("HSV",horizontal_img)

    # CREATE THE HSV FROM THE BGR IMAGE

    image_hsv = cv2.cvtColor(horizontal_img, cv2.COLOR_BGR2HSV)

    # CALLBACK FUNCTION
    cv2.setMouseCallback("HSV",pick_color)

release = cap.release()
cv2.destroyAllWindows()




