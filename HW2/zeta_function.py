import numpy as np

def integration(a,b,fun):
    delta = (b-a) / 20000
    sum = 0
    for i in range(10000):
        sum = sum + delta * (fun(a+2*i*delta) + 4 * fun(a+(2*i+1)*delta)
         + fun(a+(2*i+2)*delta)) / 3.0
    return sum

def three_dimension_number(x,y,z):
    return x*x + y*y + z*z


def fun(x):
    return x**(-3/2)

def Z00(q):
    term1 = np.exp(q) * np.sum([np.exp(-three_dimension_number(i,j,k)) / (three_dimension_number(i,j,k) - q)
     for i in range (-4,5) for j in range(-4,5) for k in range(-4,5)]) / 2*np.sqrt(np.pi)

    term2 = np.pi*np.sum([q**m/(np.math.factorial(m)*(m-1/2)) for m in range(1, 18)])/2