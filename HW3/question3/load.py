import numpy as np
import matplotlib.pyplot as plt
import jackknife as jackk

'''
concatanate 200 files into one file
'''
def concat():
    a = open("./data2.dat",'w')
    number = 1000
    for i in range(220):
        name = "./data/traj_{}_pion.txt".format(number)
        lines = open(name).readlines()
        for line in lines:
            a.write(line)
        number = number +10
    a.close()

'''
load data from file, symmetrize, return a 200x32 numpy array
'''
def loadData(filename):
    lines = open(filename).readlines()[:]
    res = []
    for line in lines:
        slt = line.split()
        res.append(float(slt[1]))
        #assert float(slt[2]) == 0
    ans = np.array(res)

    data = ans.reshape(-1,32)

    #C0 = data[:,0].reshape(200,1)
    #Ct = (data[:,1:33] + data[:,63:31:-1]) * 0.5
    #C = np.concatenate([C0,Ct],axis=1)
    
    return data

if __name__ == "__main__":
    concat()
    #loadData('data2.dat')