import numpy as np
from matplotlib import pyplot as plt
import interpolation as itl

t = np.arange(9)
phi = np.array([t0*np.pi/4.0 for t0 in t])
x_exact = np.array([(1-np.cos(t0*np.pi/4.0))*np.cos(t0*np.pi/4.0) for t0 in t])
y_exact = np.array([(1-np.cos(t0*np.pi/4.0))*np.sin(t0*np.pi/4.0) for t0 in t])

# file1 = open(r'./running_results/cardioid_exact.txt','w')
# for i in range(9):
#     string = "|{:.4f}|".format(x[i]) + "{:.4f}| \n".format(y[i])
#     file1.write(string)
# file1.close()

t_in = np.linspace(0,8,81)
X,MX,hX,AX,BX = itl.spline(x_exact,t,0,0,t_in)
Y,MY,hY,AY,BY = itl.spline(y_exact,t,0,0,t_in)

# file2 = open(r'./running_results/spline_coeffcients.txt','w')
# for i in range(0,8):
#     a = - MX[i] / (6 * hX[i+1])
#     b = - MX[i+1] / (6 * hX[i+1])
#     string = "|{}".format(i) + "|{:.4f}".format(a) +  "|{:.4f}".format(b) + "|{:.4f}".format(AX[i]) + "|{:.4f}".format(BX[i]) + "| \n"
#     file2.write(string)

# for j in range(0,8):
#     a = - MY[j] / (6 * hY[j+1])
#     b = - MY[j+1] / (6 * hY[j+1])
#     string = "|{}".format(j) + "|{:.4f}".format(a) +  "|{:.4f}".format(b) + "|{:.4f}".format(AY[j]) + "|{:.4f}".format(BY[j]) + "| \n"
#     file2.write(string)

# file2.close()   

X_e = np.array([(1-np.cos(t0*np.pi/4.0))*np.cos(t0*np.pi/4.0) for t0 in t_in])
Y_e = np.array([(1-np.cos(t0*np.pi/4.0))*np.sin(t0*np.pi/4.0) for t0 in t_in])

plt.figure(figsize=(8, 6), dpi=80)
plt.subplot(1, 1, 1)
#plt.plot(t_in,X)
plt.plot(X, Y,'o--',markersize='2',color='b')
plt.plot(X_e, Y_e, color="red", alpha=1.00)
plt.scatter(x_exact, y_exact, 50, color="green")
#plt.show()
plt.savefig("./running_results/cardioid.png")