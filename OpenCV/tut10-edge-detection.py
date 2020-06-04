#Edge Detection and Gradient
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_,frame = cap.read()
	#hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	cv2.imshow('frame',frame)

	laplacian = cv2.Laplacian(frame, cv2.CV_64F)
	sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5)
	sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 5)

	#There are different types of inbuilt edge detectors. Here we are using Canny
	edges = cv2.Canny(frame, 100, 200)
	#based on these two parameter the range of edges is determined
	cv2.imshow('laplacian',laplacian)
	cv2.imshow('sobelx', sobelx)
	cv2.imshow('sobely', sobely)
	cv2.imshow('Edges',edges)



	k = cv2.waitKey(1) & 0xFF == ord('q')
	if k == True:
		break

cv2.destroyAllWindows()
cv2.release()
	
