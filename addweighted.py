import cv2
import numpy as np
img1 = cv2.imread('maomao.png',cv2.IMREAD_REDUCED_COLOR_2)
img2 = cv2.imread('mygo_logo.jpg',cv2.IMREAD_REDUCED_COLOR_2)
#图像融合必须要统一大小，类型和通道数
#统一尺寸
height, width= img1.shape[:2]
img2_rezised = cv2.resize(img2,(width,height))
#统一代码^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
img3 = cv2.addWeighted(img1,0.8,img2_rezised,0.2,0)
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.waitKey(0)