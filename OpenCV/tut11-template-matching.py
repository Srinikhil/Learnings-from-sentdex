import cv2
import numpy as np
#img_bgr = cv2.imread('temp_try_pic.jpg')
img_bgr = cv2.imread('small_flowers_pic.jpg')
img_gray = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)

#template = cv2.imread('temp_try_temp1.jpg',0)
template = cv2.imread('small_flowers_temp.jpg',0)
w, h = template.shape[::-1]
print(np.shape(template))

#print(template.shape[::-1])

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.5
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
	cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)

while True:
	cv2.imshow('detected', img_bgr)


	k = cv2.waitKey(1) & 0xFF == ord('q')
	if k == True:
		break
cv2.destroyAllWindows()
cv2.release()

