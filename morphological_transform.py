import cv2
import numpy as np

while(1):
    cap = cv2.VideoCapture(0)
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    dim = (350, 350)
    frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    rgb = frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([32,28,95])
    upper_red1 = np.array([164,161,255])

    lower_red = np.array([147,98,93])
    upper_red = np.array([199, 198, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    mask1 = cv2.inRange(rgb,lower_red1,upper_red1)
    #cv2.imshow("Mask",mask)
    #cv2.imshow("Mask1", mask1)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    res1 = cv2.bitwise_and(frame, frame,mask=mask1)
    kernel = np.ones((3,3),np.uint8)
    erosion = cv2.erode(mask,kernel,iterations = 1)
    erosion1 = cv2.erode(mask1, kernel, iterations=1)
    dilation = cv2.dilate(erosion,kernel,iterations = 1)
    #mix = np.logical_and(erosion,dilation)
    #cv2.imshow('Original',frame)
    add = erosion & dilation
    end = (erosion & erosion1)
    lower_white = np.array([0, 0, 0])
    upper_white = np.array([25, 25, 25])

    mask = cv2.inRange(hsv, lower_white, upper_white)
    res = cv2.bitwise_and(end, end, mask=mask)

    edges = cv2.Canny(end, 100, 200)
    final = np.zeros((350, 350,3))
    height,width = edges.shape[:2]
    for i in range(0, height):
        for j in range(0, width):
            pixel_edges = np.uint8(edges[i,j])
            if(pixel_edges >= np.uint8(235)):
                final[i,j,2] = 255
            else :
                final[i,j,0] = 0
                final[i,j,1] = 0
                final[i, j, 2] = 0
    cv2.imshow('Edges', end)
    cv2.imshow("end",final)
    #cv2.imshow('Dilation',dilation)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
'''
cap = cv2.VideoCapture(1)

while(1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    kernel = np.ones((5,5),np.uint8)
    
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('Original',frame)
    cv2.imshow('Mask',mask)
    cv2.imshow('Opening',opening)
    cv2.imshow('Closing',closing)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
'''
