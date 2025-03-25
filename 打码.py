import cv2
src1 = cv2.imread('soyoshupian.jpg')
cv2.imshow('soyoshupian', src1)
src1[240:280,320:380] = 0
cv2.imshow('soyoshupian', src1)
cv2.waitKey(0)