import cv2

src1 = cv2.imread('soyotea.jpg',cv2.IMREAD_REDUCED_COLOR_2)
src2 = cv2.imread('tuoyuan.jpg', cv2.IMREAD_REDUCED_COLOR_2)

height, width= src1.shape[:2]
src2_rezised = cv2.resize(src2,(width,height))

img3 = cv2.bitwise_and(src1,src2_rezised)
cv2.imshow('src1',src1)
cv2.imshow('src2',src2)
cv2.imshow('img3',img3)
cv2.waitKey(0)

