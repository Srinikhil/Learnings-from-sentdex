import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('F:\Adobe photoshop\images.jpg',0)
# IMREAD_GRAYSCALE = 0
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.plot([0,100],[0,100],'c',linewidth = 5)
plt.show()

cv2.imwrite('Deepika.jpg',img) # saves image into our directory