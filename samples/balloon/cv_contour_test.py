import numpy as np
import cv2

im = cv2.imread('../../datasets/branch/test/IMG_1067.JPG')
# cv2.imshow(im)

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
print(thresh)
img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

img = cv2.drawContours(img, contours, -1, (0,255,0), 3)
