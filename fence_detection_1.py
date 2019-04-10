import numpy as np
import cv2
import sys
import tkinter as tk

while (1):
    thresh_low_hsv = np.array([0,37,0])
    thresh_high_hsv = np.array([28,146,215])
    thresh_low_rgb = np.array([15,18,2])
    thresh_high_rgb = np.array([152,169,213])
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    dim = (100,100)
    frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    horizontal_img = cv2.flip(frame, 1)
    rgb = horizontal_img
    hsv = cv2.cvtColor(horizontal_img, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV",hsv)
    cv2.imshow("RGB",rgb)
    height, width = frame.shape[:2]
    i = 0
    j = 0
    final = np.zeros((150, 150, 3))
    for i in range(0, height):
        for j in range(0, width):
            pixel_hsv = np.uint8([hsv[i, j, 0],hsv[i, j, 1],hsv[i, j, 2]])
            pixel_rgb = np.uint8([rgb[i, j, 0],rgb[i, j, 1],rgb[i, j, 2]])
            if np.logical_and(pixel_hsv[0] >= thresh_low_hsv[0], pixel_hsv[0] <= thresh_high_hsv[0]):
                if np.logical_and(pixel_rgb[0] >= thresh_low_rgb[0] , pixel_rgb[0] <= thresh_high_rgb[0]):
                    final[i, j, 0] = 255;
                else:
                    final[i, j, 0] = 0;
                    final[i, j, 1] = 0;
                    final[i, j, 2] = 0;
            else:
                final[i, j, 0] = 0;
                final[i, j, 1] = 0;
                final[i, j, 2] = 0;

            if np.logical_and(pixel_hsv[1] >= thresh_low_hsv[1] , pixel_hsv[1] <= thresh_high_hsv[1]) :
                if np.logical_and(pixel_rgb[1] >= thresh_low_rgb[1] , pixel_rgb[1] <= thresh_high_rgb[1]) :
                    final[i, j, 1] = 255;
                else:
                    final[i, j, 0] = 0;
                    final[i, j, 1] = 0;
                    final[i, j, 2] = 0;
            else:
                final[i, j, 0] = 0;
                final[i, j, 1] = 0;
                final[i, j, 2] = 0;

            if np.logical_and(pixel_hsv[2] >= thresh_low_hsv[2] , pixel_hsv[2] <= thresh_high_hsv[2]) :
                if np.logical_and(pixel_rgb[2] >= thresh_low_rgb[2] , pixel_rgb[2] <= thresh_high_rgb[2]) :
                    final[i, j, 2] = 255;
                else:
                    final[i, j, 0] = 0;
                    final[i, j, 1] = 0;
                    final[i, j, 2] = 0;
            else:
                final[i, j, 0] = 0;
                final[i, j, 1] = 0;
                final[i, j, 2] = 0;

    dim = (1280, 720)
    final = cv2.resize(final, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("end", final)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

release = cap.release()
cv2.destroyAllWindows()
