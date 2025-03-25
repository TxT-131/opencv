import cv2
import numpy as np
img1 = cv2.imread('maomao.png', cv2.IMREAD_REDUCED_COLOR_2)
img2 = cv2.imread('mygo_logo.jpg',cv2.IMREAD_REDUCED_COLOR_2)
height, width= img1.shape[:2]
img2_rezised = cv2.resize(img2,(width,height))
img3 = img1 + img2_rezised
img4 = cv2.add(img1,img2_rezised)
cv2.imshow('cos1',img1)
cv2.imshow('cos2',img2)
cv2.imshow('cos1 + cos2',img3)
cv2.imshow('cos1 add cos2',img4)
cv2.waitKey(0)
