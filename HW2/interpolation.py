import numpy as np
import matplotlib.pyplot as plt
import copy

# solve three diagonal matrix generally
def solve_three_diag_mat(a,b,c,Y):
    N = np.size(a)
    nb = np.size(b)
    nc = np.size(c)
    ny = np.size(Y)
    assert nb == N-1, 'incompatible a and b'
    assert nc == N-1, 'incompatible a and c'
    assert ny == N, 'incompatible a and y'

    b_new = np.zeros(N)
    b_new[1:] = b
    alpha = np.zeros(N)
    beta = np.zeros(N)

    #build L & U
    alpha[0] = a[0]
    beta[0] = 0.0
    for i in range (1,N):
        beta[i] = b_new[i] / alpha[i-1]
        alpha[i] = a[i] - beta[i]*c[i-1]

    # solve Ly = Y
    y = np.zeros(N)
    y[0] = Y[0]
    for k in range(1,N):
        y[k] = Y[k] - beta[k]*y[k-1]
    
    #solve UX = y
    X = np.zeros(N)
    X[N-1] = y[N-1] / alpha[N-1]
    for l in range(N-2,-1,-1):
        X[l] = (y[l] - c[l]*X[l+1])/alpha[l]    

    return X

'''
Polynomial function
Input:
1.f: numpy array of input function value on corresponding xin
2.xin: numpy array of nodes x-coordinates for spline
3.x0: input ONE x-coordinate that you want to know the value using polynomial interpolation
Output:
Corresponding interpolation value on x0
'''
def neville(xin,f,x0):
    n = np.size(f)
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
Spline function 
Note: Here I use 3rd boundary condition, which means f'(a) = S'(x0),f'(b)=S'(xn)
input:
1.f: numpy array of input function value on corresponding xin
2.xin: numpy array of nodes x-coordinates for spline
3.diffa,diffb: function differential value at left end and right end
4.x: input numpy array of x-coordinates that you want to know the value using spline interpolation
output:
1. numpy array of corresponding spline value of x
2. numpy array of spline coefficients M
'''
def spline(f,xin,diffa,diffb,x):
    N = np.size(xin)
    n = N -1

    #generate h
    h = np.zeros(N+1) 
    for i in range(1,N):
        h[i] = xin[i]-xin[i-1]

    a = np.zeros(N)
    b = np.zeros(n)
    c = np.zeros(n)
    Y = np.zeros(N)

    #generate the matrix
    for i in range(0, N):
        a[i] = (h[i] + h[i+1]) /3.0
    for i in range(0,n):
        b[i] = h[i+1] / 6.0
        c[i] = h[i+1] / 6.0

    Y[0] = (f[1]-f[0]) / h[1] -diffa
    for j in range(1,n):
        Y[j] = (f[j+1] - f[j]) / h[j+1] - (f[j] - f[j-1]) / h[j]
    Y[n] = diffb - (f[n]-f[n-1]) / h[n]

    M = solve_three_diag_mat(a,b,c,Y)

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
    
    return np.array(output),M,h,A,B

######################
# Input Parameters
######################
# for interpolation and appoximation
def fun(x):
    return 1.0 / (1 + 25.0 * x * x)
xin = np.linspace(-1,1,21)
f = 1.0 / (1 + 25.0 * xin * xin)

# test points
x = np.linspace(-1,1,41)
x_che = [np.cos(np.pi*(k/2+0.5)/20) if abs(int(k/2)*2-k) <
      1e-6 else (np.cos(np.pi*(k/2)/20)+np.cos(np.pi*(k/2+1)/20))/2 for k in range(2*20-1)]

#plt.figure(figsize=(15,12))

# ####################
# #  neville method
# ####################
# inter = []
# for x1 in x:
#     ans = neville(xin,f,x1)
#     inter.append(ans)
# ne = np.array(inter)

# plt.subplot(1,1,1)
# plt.plot(x,ne,'o--',markersize='3',color='r')
# ytemp = [fun(x1) for x1 in x]
# y=np.array(ytemp)
# plt.plot(x,y,'-')
# plt.ylim(-1.0,1.5)
# #plt.show()
# plt.savefig("./running_results/neville.png")

# file1 = open(r'./running_results/neville.txt','w')
# for i in range(0,41):
#     xwrite = "|{:.2f}".format(x[i])
#     fwrite = "|{:.7f}".format(fun(x[i]))
#     nwrite = "|{:.7f}".format(ne[i])
#     delta = ne[i] - fun(x[i])
#     dwrite = "|{:.7f}".format(delta)
#     file1.write(xwrite)
#     file1.write(fwrite)
#     file1.write(nwrite)
#     file1.write(dwrite)
#     file1.write("| \n")
# file1.close()


# ######################
# #     Chebyshev
# ######################
# c = chebyshev(fun,20,x_che)
# plt.subplot(1,1,1)
# plt.plot(x_che,c,'o--',markersize='3',color='r')
# ytemp = [fun(x1) for x1 in x_che]
# y=np.array(ytemp)
# plt.plot(x_che,y,'-')
# plt.ylim(-1.0,1.5)
# #plt.show()
# plt.savefig("./running_results/chebyshev.png")

# file2 = open(r'./running_results/chebyshev.txt','w')
# for i in range(0,39):
#     xwrite = "|{:.7f}".format(x_che[i])
#     fwrite = "|{:.7f}".format(fun(x_che[i]))
#     cwrite = "|{:.7f}".format(c[i])
#     delta = c[i] - fun(x_che[i])
#     dwrite = "|{:.7f}".format(delta)
#     file2.write(xwrite)
#     file2.write(fwrite)
#     file2.write(cwrite)
#     file2.write(dwrite)
#     file2.write("| \n")
# file2.close()

# ######################
# #     Spline
# ######################
# sp = spline(f,xin,0.0739645,-0.0739645,x)
# sp = sp[0]
# plt.subplot(1,1,1)
# plt.plot(x,sp,'o--',markersize='3',color='r')
# ytemp = [fun(x1) for x1 in x]
# y=np.array(ytemp)
# plt.plot(x,y,'-')
# plt.ylim(-1.0,1.5)
# #plt.show()
# plt.savefig("./running_results/spline.png")

# file3 = open(r'./running_results/spline.txt','w')
# for i in range(0,41):
#     xwrite = "|{:.2f}".format(x[i])
#     fwrite = "|{:.7f}".format(fun(x[i]))
#     awrite = "|{:.7f}".format(sp[i])
#     delta = sp[i] - fun(x[i])
#     dwrite = "|{:.7f}".format(delta)
#     file3.write(xwrite)
#     file3.write(fwrite)
#     file3.write(awrite)
#     file3.write(dwrite)
#     file3.write("| \n")
# file3.close()