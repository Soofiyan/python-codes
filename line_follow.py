'''
# import the required library 
import numpy as np 
import cv2 
from matplotlib import pyplot as plt 
  
  
# read the image 
img = cv2.imread('corner1.png') 
  
# convert image to gray scale image 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
# detect corners with the goodFeaturesToTrack function. 
corners = cv2.goodFeaturesToTrack(gray, 27, 0.01, 10) 
corners = np.int0(corners) 
  
# we iterate through each corner,  
# making a circle at each point that we think is a corner. 
for i in corners: 
    x, y = i.ravel() 
    cv2.circle(img, (x, y), 3, 255, -1) 
  
plt.imshow(img), plt.show()

'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    grayscaled = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv1 = cv2.cvtColor(hsv, cv2.COLOR_BGR2GRAY) 
    lower_white = np.uint8([[[100,0,0]]])
    upper_white = np.uint8([[[255,255,255]]])
    th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    mask = cv2.inRange(hsv1, lower_white, upper_white)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    corners = cv2.goodFeaturesToTrack(mask, 27, 0.01, 10)
    corners = np.int0(corners)
    for i in corners: 
        x, y = i.ravel() 
        cv2.circle(frame, (x, y), 3, 255, -1)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('thres',th)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
