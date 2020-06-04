# Blurring and Smoothing

#smoothing and blurring are done for tut7

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
    
    kernel = np.array((15,15),np.float32)/225 # 15 * 15 = 225 average of pixels
    smoothed = cv2.filter2D(res,-1,kernel)
   # cv2.imshow('smoothed',smoothed)
   
    blur = cv2.GaussianBlur(res,(15,15),0)
  # cv2.imshow('GBlur',blur)
    
    median = cv2.medianBlur(res,15)
   # cv2.imshow('medianblur',median)
    
    bilateral = cv2.bilateralFilter(res,15,75,75)
    cv2.imshow('bilateral',bilateral)
    
    k = cv2.waitKey(1) & 0xFF == ord('q')
    if k == True:
        break
        
    
cv2.destroyAllWindows()
cap.release()