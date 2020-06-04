#Arithmetic and Logic

import cv2
import numpy as np

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainlogo.png')
#add = img1 + img2
#add = cv2.add(img1*10,img2*100) # two pixel values are added
#weighted = cv2.addWeighted(img1,0.6,img2,0.4,0)#imposing one image on other with ratio of opaquenes
#                       POO of img1  POO of img2  gamma  -->POO Percentage Of Opaqueness

rows,columns,channels = img2.shape
roi = img1[0:rows,0:columns]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV) #Creates a mask like in photoshop with pixels greater than 220 is made white(255)
cv2.imshow('mask',mask)

mask_inv = cv2.bitwise_not(mask) #inverting white and black areas (logical not)
cv2.imshow('mask_inv',mask_inv)

img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
cv2.imshow('img1_bg',img1_bg)

img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
cv2.imshow('img2_fg',img2_fg)

dst = cv2.add(img1_bg,img2_fg)
cv2.imshow('dst',dst)

img1[0:rows,0:columns] = dst
cv2.imshow('final image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()