import numpy as np
rng = np.random.default_rng()
a = rng.integers(10,size=8)
print(a)
print(a[0])
print(a[-1])
print(a[2])
print(a[2:5])
print(a[:2])
print(a[5:])
for x in a:
    print(x,end='')


rng = np.random.default_rng()
a=rng.integers(10,size=(2,5))
print(a)
print(a[0,0])
print(a[1,0])
print(a[0,:3])
for x in a:
    print(x)