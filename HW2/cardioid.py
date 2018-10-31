import numpy as np
from matplotlib import pyplot as plt
import interpolation as itl

t = np.arange(9)
phi = np.array([t0*np.pi/4.0 for t0 in t])
x_exact = np.array([(1-np.cos(t0*np.pi/4.0))*np.cos(t0*np.pi/4.0) for t0 in t])
y_exact = np.array([(1-np.cos(t0*np.pi/4.0))*np.sin(t0*np.pi/4.0) for t0 in t])

# file1 = open(r'cardioid_exact.txt','w')
# for i in range(9):
#     string = "|{:.4f}|".format(x[i]) + "{:.4f}| \n".format(y[i])
#     file1.write(string)
# file1.close()

t_in = np.linspace(0,8,81)
X = itl.spline(x_exact,t,0,0,t_in)
Y = itl.spline(y_exact,t,1,1,t_in)

X_e = np.array([(1-np.cos(t0*np.pi/4.0))*np.cos(t0*np.pi/4.0) for t0 in t_in])
Y_e = np.array([(1-np.cos(t0*np.pi/4.0))*np.sin(t0*np.pi/4.0) for t0 in t_in])

plt.figure(figsize=(8, 6), dpi=80)
plt.subplot(1, 1, 1)
plt.plot(t_in,X)
# plt.plot(X, Y,'o',markersize='3',color='b')
# plt.plot(X_e, Y_e, color="red", alpha=1.00)
# plt.scatter(x_exact, y_exact, 20, color="blue")
plt.show()