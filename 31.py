import cv2
import numpy
import numpy as np
img = numpy.zeros((240,320),dtype=numpy.uint8)
img[70:170,110:210]=255
cv2.namedWindow('test31',cv2.WINDOW_NORMAL)
cv2.imshow('test31',img)
cv2.waitKey(0)


# cv2.destroyAllWindows()
# cv2.destroyAllWindows('test31')
img1 = cv2.imread('soyotea.jpg')
s = img1.shape
cv2.imshow('test31',img1)
key = cv2.waitKey(500)
cv2.resizeWindow('test31',(s[0]//2,s[1]//2))
cv2.waitKey(0)

