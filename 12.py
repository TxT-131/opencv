import cv2
img = cv2.imread('cos1.jpg',cv2.IMREAD_REDUCED_COLOR_2)
cv2.imshow('cos1',img)
b,g,r = cv2.split(img)
rgb = cv2.merge((b,g,r))
gbr = cv2.merge((g,b,r))
cv2.imshow('RGB',rgb)
cv2.imshow('GBR',gbr)
cv2.waitKey(0)
