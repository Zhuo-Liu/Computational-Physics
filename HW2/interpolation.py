import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Chebyshev as Cbs
import copy

def neville(xin,f,x0):
    n = np.size(f)
    T0 = np.zeros(n)
    T0 = copy.deepcopy(f)
    T1 = np.zeros(n)
    for k in range(1,n):
        for j in range(k,n):
            T1[j] = ((x0-xin[j-k])*T0[j] - (x0-xin[j])*T0[j-1]) / (xin[j]-xin[j-k])
        T0 = copy.deepcopy(T1)
        T1[:] = 0.0
    
    return T0[n-1]

'''
Chebyshev Approximation
Input:
1.fn: input function
2.N: number of nodes for approximation
3.x: input numpy array of x-coordinates that you want to know the value using chebyshev approximation
Output:
numpy array of corresponding approximated value on x
'''
def chebyshev(fn,N,x):
    coeff=[]

    for m in range(0,N):
        cm = 0.0
        for k in range(0,N):
            cos = np.cos(np.pi*(k+0.5)/N)
            ctemp = fn(cos) * np.cos(np.pi*(k+0.5)*m/N)
            cm = cm + ctemp
        cm = 2.0*cm / N
        coeff.append(cm)
    
    n = np.size(x)
    ans = []
    for i in range(0,n):
        sum = 0.0
        for j in range(0,N):
            sum = sum + coeff[j]*np.cos(j*np.arccos(x[i]))
        fn = - 0.5 * coeff[0] + sum
        ans.append(fn)

    return np.array(ans)

'''
spline function
input:
1.f: numpy array of input function value on corresponding xin
2.xin: numpy array of nodes x-coordinates for spline
3.diffa,diffb: function differential value at left end and right end
4.x: input numpy array of x-coordinates that you want to know the value using spline function
output:
numpy array of corresponding spline value of x
'''
def spline(f,xin,diffa,diffb,x):
    N = np.size(xin)
    n = N -1
    alpha = np.zeros(N)
    beta = np.zeros(n)
    h = np.zeros(N+1)

    #generate h
    for i in range(1,N):
        h[i] = xin[i]-xin[i-1]
  
    #generate the matrix
    alpha[0] = (h[0] + h[1]) / 3.0
    for i in range(1,N):
        beta[i-1] = h[i]/ (6.0*alpha[i-1])
        alpha[i] = (h[i] + h[i+1])/3.0 - beta[i-1]*h[i] / 6.0

    #set Y value
    Y = np.zeros(N)
    Y[0] = (f[1]-f[0]) / h[1] - diffa
    for j in range(1,n):
        Y[j] = (f[j+1] - f[j]) / h[j+1] - (f[j] - f[j-1]) / h[j]
    Y[n] = diffb - (f[n]-f[n-1]) / h[n]

    #solve L*y=Y
    y = np.zeros(N)
    y[0] = Y[0]
    for k in range(1,N):
        y[k] = Y[k] - beta[k-1]*y[k-1]
    
    #solve U*M=y
    M = np.zeros(N)
    M[n] = y[n]
    for l in range(n-1,-1,-1):
        M[l] = (y[l+1] - (h[l] / 6.0)*x[l+1])/alpha[l]

    B = np.zeros(n)
    A = np.zeros(n)
    
    for j in range(0,n):
        B[j] = f[j] - M[j]*h[j+1]*h[j+1] / 6.0
        A[j] = (f[j+1]-f[j])/h[j+1] - h[j+1] * (M[j+1]-M[j])/6.0
    
    #output part
    num = np.size(x)
    output=[]
    for i in range(0,num):
        t=0
        delta = x[i] - xin[0]
        while(delta>0 or delta==0):
            t=t+1
            delta = delta - h[t]
            if(t==N):
                t = t-1
                break

        temp =  M[t-1] * (xin[t]-x[i])**3 / (6.0*h[t]) + M[t]*(x[i]-xin[t-1])**3 / (6.0*h[t]) + A[t-1]*(x[i]-xin[t-1]) + B[t-1]
        output.append(temp)
    
    return np.array(output)

# ##################
# #    Input
# ##################
def fun(x):
    return 1.0 / (1 + 25.0 * x * x)
xin = np.linspace(-1,1,21)
f = 1.0 / (1 + 25.0 * xin * xin)
x = np.linspace(-1,1,41)
x_che = [np.cos(np.pi*(k/2+0.5)/20) if abs(int(k/2)*2-k) <
      1e-6 else (np.cos(np.pi*(k/2)/20)+np.cos(np.pi*(k/2+1)/20))/2 for k in range(2*20-1)]
# #####################

# plt.figure(figsize=(15,12))
# ####################
# #  neville method
# ####################
# inter = []
# for x1 in x:
#     ans = neville(xin,f,x1)
#     inter.append(ans)
# ne = np.array(inter)

# plt.subplot(1,3,1)
# plt.plot(x,ne,'o--',markersize='3',color='r')
# ytemp = [fun(x1) for x1 in x]
# y=np.array(ytemp)
# plt.plot(x,y,'-')
# plt.ylim(-1.0,1.5)
# plt.show()

# file1 = open(r'neville.txt','w')
# for i in range(0,41):
#     xwrite = "|{}".format(x[i])
#     fwrite = "|{}".format(fun(x[i]))
#     nwrite = "|{}".format(ne[i])
#     delta = ne[i] - fun(x[i])
#     dwrite = "|{}".format(delta)
#     file1.write(xwrite)
#     file1.write(fwrite)
#     file1.write(nwrite)
#     file1.write(dwrite)
#     file1.write("| \n")
# file1.close()


# ######################
# #     Chebychev
# ######################
# c = chebyshev(fun,20,x_che)
# plt.subplot(1,3,2)
# plt.plot(x_che,c,'o--',markersize='3',color='r')
# ytemp = [fun(x1) for x1 in x_che]
# y=np.array(ytemp)
# plt.plot(x_che,y,'-')
# plt.ylim(-1.0,1.5)
# plt.show()

# file2 = open(r'chebyshev.txt','w')
# for i in range(0,39):
#     xwrite = "|{}".format(x_che[i])
#     fwrite = "|{}".format(fun(x_che[i]))
#     cwrite = "|{}".format(c[i])
#     delta = c[i] - fun(x_che[i])
#     dwrite = "|{}".format(delta)
#     file2.write(xwrite)
#     file2.write(fwrite)
#     file2.write(cwrite)
#     file2.write(dwrite)
#     file2.write("| \n")
# file2.close()

# ######################
# #     Spline
# ######################
sp = spline(f,xin,0.0739645,-0.0739645,x)
plt.subplot(1,1,1)
plt.plot(x,sp,'o--',markersize='3',color='r')
ytemp = [fun(x1) for x1 in x]
y=np.array(ytemp)
plt.plot(x,y,'-')
plt.ylim(-1.0,1.5)
plt.show()

# file3 = open(r'spline.txt','w')
# for i in range(0,41):
#     xwrite = "|{}".format(x[i])
#     fwrite = "|{}".format(fun(x[i]))
#     awrite = "|{}".format(sp[i])
#     delta = sp[i] - fun(x[i])
#     dwrite = "|{}".format(delta)
#     file3.write(xwrite)
#     file3.write(fwrite)
#     file3.write(awrite)
#     file3.write(dwrite)
#     file3.write("| \n")
# file3.close()