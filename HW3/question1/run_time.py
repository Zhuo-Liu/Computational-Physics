import householder as hh
import givens as gv
import numpy as np
import time
import matplotlib.pyplot as plt

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

time1 = np.array(time1)
time2 = np.array(time2)
print(time1)
print(time2)

output = open('run_time.txt','w')

for i in range(len(time1)):
    line2 = "|{}".format(i+3) +"|{:.5f}|".format(time1[i]) + "{:.5f}| \n".format(time2[i])
    output.write(line2)
output.close()

# time1,=plt.plot(np.arange(3,30),time1,'o-',label='Householder')
# time2,=plt.plot(np.arange(3,30),time2,'o-',label='Givens')
# plt.ylabel('time/s',fontsize='x-large')
# plt.xlabel('n',fontsize='x-large')
# plt.legend([time1,time2],["Householder","Givens"],loc='upper center', bbox_to_anchor=(0.1,0.9), fontsize='large')

# plt.savefig('run_time.jpg')
# plt.show()