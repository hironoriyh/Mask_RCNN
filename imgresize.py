import numpy as np
import cv2
import glob
image_list = []


for filename in glob.glob('datasets/temp/*.jpg'): #assuming gif
    # print(filename)
    im=cv2.imread(filename)
    # image_list.append(im)
    # img = image_list[0]
    orgHeight, orgWidth = im.shape[:2]
    print(orgWidth, orgHeight )
    size = (1024, int(1024*orgHeight/orgWidth))
    print(orgHeight, orgWidth, size,)
    small_img = cv2.resize(im, size)
    cv2.imwrite(filename, small_img)

# print(image_list[0])
# im = cv2.imread(image_list[0])
# img = image_list[0]
# orgHeight, orgWidth = img.shape[:2]
# size = (1024, int(1024*orgHeight/orgWidth))
# print(orgHeight, orgWidth, size,)
# small_img = cv2.resize(img, size)
# cv2.imwrite('half.jpg', small_img)

# cv2.imshow(im)

# imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# ret,thresh = cv2.threshold(imgray,127,255,0)
# print(thresh)
# img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
#
# img = cv2.drawContours(img, contours, -1, (0,255,0), 3)
