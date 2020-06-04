# Color Filtering
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
    cv2.imshow('mask',mask)
    res = cv2.bitwise_and(frame,frame,mask = mask)
    cv2.imshow('res',res)
    
    
    k = cv2.waitKey(1) & 0xFF == ord('q')
    if k == True:
        break
        
    
cv2.destroyAllWindows()
cap.release()