import cv2
src1 = cv2.imread('soyoshupian.jpg',cv2.IMREAD_REDUCED_COLOR_2)
src2 = cv2.imread('mygo_logo.jpg',cv2.IMREAD_REDUCED_COLOR_2)
#位运算必须要统一大小，类型和通道数
#统一尺寸
height, width= src1.shape[:2]
src2_rezised = cv2.resize(src2,(width,height))

img3 = cv2.bitwise_and(src1,src2_rezised)
img4 = cv2.bitwise_or(src1,src2_rezised)
img5 = cv2.bitwise_not(src1)
img6 = cv2.bitwise_xor(src1,src2_rezised)
cv2.imshow('src1',src1)
cv2.imshow('src2',src2)
cv2.imshow('and',img3)
cv2.imshow('or',img4)
cv2.imshow('not',img5)
cv2.imshow('xor',img6)
cv2.waitKey(0)