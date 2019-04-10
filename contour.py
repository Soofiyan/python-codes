import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    rgb = frame
    lower_red = np.array([80, 38, 110])
    upper_red = np.array([106, 74, 203])
    lower_red1 = np.array([135, 131, 81])
    upper_red1 = np.array([187, 184, 173])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    mask1 = cv2.inRange(rgb,lower_red1,upper_red1)

    res = cv2.bitwise_and(frame,frame,mask=mask)
    res1 = cv2.bitwise_and(frame, frame, mask=mask1)
    ret, thresh = cv2.threshold(mask, 127, 255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    ret, thresh1 = cv2.threshold(mask1, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours1, _ = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours2 = contours and contours1;
    cv2.drawContours(frame, contours, -1, (0,255,0), 1)
    cv2.imshow("cnt1",frame)
    img = frame
    for i in contours:
        area = cv2.contourArea(i)
        if(area > 30000):
            x,y,w,h = cv2.boundingRect(i)
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)

    cv2.imshow("end",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

release = cap.release()
cv2.destroyAllWindows()