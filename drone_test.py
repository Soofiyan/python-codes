import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('drone.jpg',cv2.IMREAD_GRAYSCALE)
#reads the image and while reading it converts it to grayscale

plt.imshow(img, cmap = 'gray', interpolation = 'hermite')
#to show the image with gray attribute and interpolation 
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([1000,1000,3000],[5000,5000,4000],'y', linewidth=5)
#this plot is having 2 attribute in which 1st matrix has the x and 2nd one the y
#co ordinate, in the matrix first point is the end point of first line and the
#second one is the starting point for common lines and third is the
#end point of second line
plt.show()

cv2.imwrite('watchgray.png',img)
