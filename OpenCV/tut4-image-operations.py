#       Image Operations
import cv2
import numpy as np

img = cv2.imread('F:\Adobe photoshop\images.jpg',1)

#pxls = img[100:200,100:200]
img[100:200,100:200] = [255,255,255]

# ROI = Region Of Image
roi = img[50:150,10:150]
img[0:100,0:140] = roi # this copies a region of image into another part

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()