#Thresholding

import cv2
import numpy as np

video = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('tut6out.avi',fourcc,20.0,(640,480))

"""
retval,threshold = cv2.threshold(img,12,255,cv2.THRESH_BINARY) # thresholding image
cv2.imshow('threshold',threshold)

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # thresholding grayscaled image
retval2,thresholdgray = cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)
cv2.imshow('thresholdgray',thresholdgray)

gaus = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow('gaus',gaus)

retotsu,otsu = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('otsu',otsu)
"""
while True:
    ret,img = video.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    retval,threshold = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
    out.write(threshold)
    cv2.imshow('Threshold',threshold)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break


#cv2.imshow('Image',img)
#cv2.waitKey(0)
video.release()
out.release()
cv2.destroyAllWindows()


#Same all these can be used for images as well as Videos as above