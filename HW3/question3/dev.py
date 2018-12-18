import numpy as np
import matplotlib.pyplot as plt
import jackknife as jackk

'''
load data from file, symmetrize, return a 200x33 numpy array
'''
def loadData(filename):
    lines = open(filename).readlines()[1:]
    res = []
    for line in lines:
        slt = line.split()
        res.append(float(slt[1]))
        assert float(slt[2]) == 0
    ans = np.array(res)

    data = ans.reshape(-1,64)

    C0 = data[:,0].reshape(200,1)
    Ct = (data[:,1:33] + data[:,63:31:-1]) * 0.5
    
    C = np.concatenate([C0,Ct],axis=1)
    
    return C

# if __name__ == '__main__':    
#     C = loadData('data.dat')

#     mean = C.mean(axis=0)

#     sum = np.zeros((1,33))
#     for line in C:
#         sum = sum + (line - mean)**2
#     dev = np.sqrt(sum / (200*199))

#     rel_dev = dev / mean * 100

#     plt.plot(np.arange(0,33),np.abs(rel_dev).reshape(33,),'o-')
#     plt.ylabel("$\Delta C / C \%$",fontsize='x-large')
#     plt.xlabel('$t$',fontsize='x-large')
#     plt.savefig("3a.jpg")
#     plt.show()
#    # dev = np.sqrt()

