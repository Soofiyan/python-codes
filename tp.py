import numpy as np
import cv2
import serial
import time


i=0
img = np.zeros((512,512,3), np.uint8)
print("Start")
port="/dev/tty.HC-05-SPPDev" #This will be different for various devices and on windows it will probably be a COM port.
bluetooth=serial.Serial(port, 9600)#Start communications with the bluetooth unit
print("Connected")
bluetooth.flushInput() #This gives the bluetooth a little kick
bluetooth.write(str.encode(str(100)))

while 1: #send 5 groups of data to the bluetooth
   #print("Ping")
   #These need to be bytes not unicode, plus a number
   input_data=(bluetooth.readline())#This reads the incoming data. In this particular example it will be the "Hello from Blue" line
   input_data = (input_data.decode())#These are bytes coming in so a decode is needed
   #time.sleep(0.1) #A pause between bursts
   i = input_data
   i = int(i)

   print(i)
   if(i >= 512):
     img = np.zeros((512, 512, 3), np.uint8)
     i=0
   cv2.circle(img,(256,256), 50, (0,0,255), 1)
   cv2.circle(img,(256,256), 100, (0,0,255), 1)
   cv2.circle(img,(256,256), 175, (0,0,255), 1)
   cv2.circle(img,(256,256), 225, (0,0,255), 1)
   cv2.circle(img,(256,256), 250, (0,0,255), 1)
   cv2.line(img,(0,0),(i,i),(255,255,255),3)
   cv2.imshow('tp', img)
   i = i + 10
   cv2.waitKey(0)
bluetooth.close() #Otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob
print("Done")
cv2.destroyAllWindows()
