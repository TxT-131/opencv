import cv2
img = cv2.imread('soyo1.jpg',cv2.IMREAD_REDUCED_COLOR_2)
cv2.imshow('soyo1',img)
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]
cv2.imshow('soyo_1.0',b)
cv2.imshow('soyo_1.1',g)
cv2.imshow('soyo_1.2',r)
cv2.waitKey(0)