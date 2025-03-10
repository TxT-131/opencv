import cv2
import numpy as np
img = np.zeros((240,320),dtype=np.uint8)
n = 0
while True:
    cv2.imshow('GrayImg',img)
    n+=20
    img[:,:] = n
    print(img[1,1])
    key = cv2.waitKey(1000)
    if key == 27:
        break