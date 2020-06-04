import cv2
import numpy as numpy 

cap =cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('tut2out.avi',fourcc,20.0,(640,480))

while True:
    ret,img = cap.read()
    #cv2.imshow('frame',img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    out.write(img)
    cv2.imshow('grayframe',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.release()
out.release()
cv2.destroyAllWindows()