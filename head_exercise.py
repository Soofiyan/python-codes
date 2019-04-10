import cv2
import numpy as np
import serial
import time



print("Start")
port="/dev/tty.HC-05-SPPDev" #This will be different for various devices and on windows it will probably be a COM port.
bluetooth=serial.Serial(port, 9600)#Start communications with the bluetooth unit
print("Connected")
#img = cv2.namedWindow('output', cv2.WINDOW_AUTOSIZE)
err_pitch = 0
err_yaw = 0
i=0
check = 0
pitch1 = 0
pitch2 = 0
yaw1 = 0
yaw2 = 0
prev_pitch = 0
prev_yaw = 0
s_check = 0

while 1:
    if (s_check == 0) :
        bluetooth.flushInput()  # This gives the bluetooth a little kick
        i = '100'
        bluetooth.write(str.encode(str(i)))
    img = np.zeros((720, 720, 3), np.uint8)
    cv2.circle(img, ((int(err_pitch*2)), (int(err_yaw*2))), 5, (0, 0, 255), -1)
    cv2.imshow('tp', img)
    input_data1 = bluetooth.readline()  # This reads the incoming data. In this particular example it will be the "Hello from Blue" line
    input_data1 = input_data1.decode()  # These are bytes coming in so a decode is needed
    input_data = int(input_data1)
    #print(input_data)
    print(input_data);
    if(input_data == 220):
        check = 1
    elif(input_data == 221):
        check = 2
    elif(input_data == 222):
        check = 3
    elif(input_data == 223):
        check = 4
    else:
        if(check == 1):
            pitch1 = input_data
        elif(check == 2):
            pitch2 = input_data
        elif(check == 3):
            yaw1 = input_data
        elif(check == 4):
            yaw2 = input_data

    if(pitch1 == 0):
        if(pitch2 == 0):
            pitch = 0
        else:
            pitch = pitch2 + 180
    else:
        pitch = pitch1

    if (yaw1 == 0):
        if (yaw2 == 0):
            yaw = 0
        else:
            yaw = yaw2 + 180
    else:
        yaw = yaw1

    err_pitch += (pitch - prev_pitch)
    err_yaw += (yaw - prev_yaw)

    prev_yaw = yaw
    prev_pitch = pitch
    it = int(err_pitch*2)
    s_check += 1;
    if(s_check >=2):
        s_check = 0;
    cv2.waitKey(1)
    #img = cv2.imread('/Users/soofiyanatar/Desktop/blank.jpg',cv2.IMREAD_COLOR)
    #img = cv2.resize(img, (720, 720))
    #print(err_pitch)
bluetooth.close() #Otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob
print("Done")
cv2.destroyAllWindows()
