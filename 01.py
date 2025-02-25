import numpy as np
import cv2
o = np.int8(123)
print(type(o))
a = np.array([1,2,3])
print(a)
print(type(a))
b = np.array((1,2,3))
c = np.array(([1,2,3],[4,5,6]))
print(b)
print(c)
# d = np.array(([1,2,3],[4,5]))
# print(d)
print(np.zeros((2, 3)))

print(np.zeros((2,5),dtype=int))

print(np.zeros((2,3,4)))

print(np.arange(5))
print(np.arange(-2,5))
print(np.arange(5.6))
print(np.arange(-2,2,dtype=float))
print(np.linspace(1, 5, 6))

print(np.indices((3, 4)))
print(np.ones((5,), dtype=int))
print(np.ones((5,)))
print(np.ones((2,5)))
print(np.ones((2,5),dtype=int))