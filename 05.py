import cv2
import numpy as np

img = cv2.imread('cos1.jpg')
print(type(img))
print(img)
print(img.shape)
print(img.dtype)
print(img.size)
# img = cv2.imread(cos1,flag)

img = cv2.imread('cos2.jpg',cv2.IMREAD_REDUCED_GRAYSCALE_4)
print(img.shape)
print(img.size)

img = np.zeros((50,50),dtype=np.uint8)
cv2.imshow('cos3-1.jpg',img)


# img = cv2.imread('cos3.jpg',cv2.IMREAD_REDUCED_COLOR_2)
# cv2.imshow('lena',img)
# cv2.waitKey(0) # 放在’imshow‘下一行，不然就闪没

img = cv2.imread('soyo1.jpg',cv2.IMREAD_REDUCED_COLOR_2)
cv2.imshow('soyo1',img)
key = 0
while key!=27:
    key = cv2.waitKey()
cv2.destroyAllWindows('soyo1')



