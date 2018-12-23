#python 3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines

from matplotlib import rcParams
rcParams['figure.figsize'] = [10, 8]

'''
RK4 Method
Input:
1. fun: the target evolving function
2. h: time step
3. N: total step
4. x0: initial x
5. y0: initial y
6. t0: initial time
Output:
x,y history list for each step
'''
def RungeKutta(fun,h,N,x0,y0,t0=0.0):
    t = t0
    x_1 = x0
    y_1 = y0
    xlist = [x0]
    ylist = [y0]
    for i in range(0,N):
        k_1 = h*fun(t,x_1,y_1)
        k_2 = h*fun(t+0.5*h,x_1+0.5*k_1[0],y_1+0.5*k_1[1])
        k_3 = h*fun(t+0.5*h,x_1+0.5*k_2[0],y_1+0.5*k_2[1])
        k_4 = h*fun(t+h,x_1+k_3[0],y_1+k_3[1])

        y_1 = y_1 + k_1[1] /6.0 + k_2[1] /3.0 + k_3[1]/3.0 + k_4[1] /6.0
        x_1 = x_1 + k_1[0] /6.0 + k_2[0] /3.0 + k_3[0]/3.0 + k_4[0] /6.0

        xlist.append(x_1)
        ylist.append(y_1)

    return xlist, ylist

def Lokta_Volterra(t,x,y,alpha=2/3,beta=4/3,gamma=1,delta=1):
    dotx = alpha * x - beta * x * y
    doty = delta * x * y - gamma * y
    return np.array([dotx, doty])

'''
for test purpose only, test for time step
'''
def timestep_test(x0s,y0s):
    t_set = [1.0,0.1,0.01,0.001]
    for t in t_set:
        x_history1, y_history1 = RungeKutta(Lokta_Volterra, t, 2, x0s[0],y0s[0])
        x_history2, y_history2 = RungeKutta(Lokta_Volterra, 2.0*t, 1, x0s[0],y0s[0])
        deltax = np.abs(x_history1[2]-x_history2[1])
        deltay = np.abs(y_history1[2]-y_history2[1])
        print((deltax,deltay))

if __name__ == "__main__":
    x0s = [0.8, 1.0,1.2,1.4,1.6]
    y0s = [0.8, 1.0,1.2,1.4,1.6]
    plot_set = []
    label_set = []
    for i in range(len(x0s)):
        x_history, y_history = RungeKutta(Lokta_Volterra, 0.001, 10000, x0s[i],y0s[i])
        string = "("+str(x0s[i])+","+str(y0s[i])+")"
        fig, = plt.plot(x_history,y_history,label=string)

        plot_set.append(fig)
        label_set.append(string)

    plt.legend(plot_set,label_set,loc='upper center', bbox_to_anchor=(0.90,0.95), fontsize='large')
    plt.title('RK4 (x,y) results for different initial conditions',fontsize='x-large')
    plt.ylabel('y',fontsize='x-large')
    plt.xlabel('x',fontsize='x-large')
    plt.savefig('result')
    plt.show()
    #timestep_test(x0s,y0s)