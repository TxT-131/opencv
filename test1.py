import cv2
import numpy as np
img = np.zeros((240, 320, 3))
img[70:170,110:210,2] = 255
cv2.imshow('img',img)
key = cv2.waitKey(0)