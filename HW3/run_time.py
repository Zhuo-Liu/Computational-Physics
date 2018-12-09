import householder as hh
import givens as gv
import numpy as np
import time

def RandomMatrix(n):
    return np.random.rand(n,n)

np.random.seed(int(time.time()))

N = list(range(3,30))
time1 = []
time2 = []

for n in N:
    A =[RandomMatrix(n) for i in range(50)]

    start1 = time.clock()
    for x in A:
        hh.HouseHolderQR(x)
    end1 = time.clock()

    start2 = time.clock()
    for x in A:
        gv.GivensQR(x)
    end2 = time.clock()

    time1.append(end1-start1)
    time2.append(end2-start2)

print(time1)
print(time2)