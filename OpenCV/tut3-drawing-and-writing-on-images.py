import cv2
import numpy as np

img = cv2.imread('F:\Adobe photoshop\images.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(100,100),(255,0,0),5) # in opencv colors are in BGR format 
cv2.rectangle(img,(10,10),(80,80),(0,255,0),2)
cv2.circle(img,(30,30),20,(0,0,255),-1) # -1 fills the shape and any other +ve n gives thickness of outer line

pts = np.array([[100,50],[150,100],[130,150],[110,150]],np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(255,255,255),3) # True -> to join first and last points,False not to join first and last points

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Hi Deepika..!',(50,100),font,1,(100,200,200),2,cv2.LINE_AA)
                #Text           strtng point size   color   thickness

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
