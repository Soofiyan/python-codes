import numpy as np

import cv2

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    #img = cv2.cvtColor(frame,0)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print(frame.shape)

    horizontal_img = cv2.flip(frame, 1)
    cv2.imshow('frame',horizontal_img)
    #cv2.imshow('gray',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

'''q
In some cases, you may actually want to record,
and save the recording to a new file.
Here's an example of doing this on Windows:

import numpy as np
import cv2

cap = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()


Mainly to note here is the codec being used,
and the output information defined before the while loop.
Then, within the while loop, we use out.write() to output the frame.
Finally, outside the while loop, after we release our
webcam, we also release the out.
'''
