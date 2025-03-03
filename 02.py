import numpy as np
import cv2

a = np.arange(12)
print(a)
print(a.shape)
a.shape=(2,-1)
print(a)
print(a.reshape((3,-1)))

# reshape 不能减少或增加数组元素个数
# a.reshape((2,3))

a.resize((3,4))
print(a)

a.resize((2,3),refcheck=False)
print(a)

a.resize((2,5),refcheck=False)
print(a)

print(np.ravel(a))

print(np.ravel(a,order='F'))