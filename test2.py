import cv2
import numpy as np
# img = cv2.imread('soyotea.jpg',cv2.IMREAD_REDUCED_GRAYSCALE_2)
# cv2.imshow('img',img)
#
#
# img2 = cv2.imread('soyotea.jpg')
# img2[200:280,280:380] = 0
# cv2.imshow('img2',img2)
#
# img3 = cv2.imread('maomao.png',cv2.IMREAD_REDUCED_COLOR_2)
# cv2.imshow('img3',img3)
# b,g,r = cv2.split(img3)
# cv2.imshow('b',b)
# cv2.imshow('g',g)
# cv2.imshow('r',r)

img4 = cv2.imread('soyotea.jpg')
# 用数组建立的图像需要保证数组的类型 保证是无符号类型
img5 = np.zeros((632,552,3),dtype=np.uint8)

img5[236:316,256:376]=255


img6 = cv2.bitwise_and(img4,img5)
cv2.imshow('img6',img6)

cv2.waitKey(0)