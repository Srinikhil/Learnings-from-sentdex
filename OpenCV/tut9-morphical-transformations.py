# Morphological Transformations

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read() # _ means it gets some value returned which we don't use
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('frame',frame)
    
    lower = np.array([150,150,50])
    upper = np.array([180,255,150])
    
    mask = cv2.inRange(hsv,lower,upper)
    #cv2.imshow('mask',mask)
    res = cv2.bitwise_and(frame,frame,mask = mask)
    cv2.imshow('res',res)
    
    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(mask,kernel,iterations= 1)
    cv2.imshow('erosion',erosion)
    
    dilation = cv2.dilate(mask,kernel,iterations = 1)
    cv2.imshow('dilation',dilation)
    
    # opening -> removes false positives in background i.e unwanted selections from background
    # closing -> removes false negatives from the selection i.e wanted selections in the required area
    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    cv2.imshow('opening',opening)
    
    closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
    cv2.imshow('closing',closing)
    
    #tophat ->difference b/w input image and opening of the image
    #blackhat -> difference b/w the closing of the image and input image
    
    k = cv2.waitKey(1) & 0xFF == ord('q')
    if k == True:
        break
        
    
cv2.destroyAllWindows()
cap.release()