import numpy as np

# integration function
def integration(a,b,fun):
    delta = (b-a) / 2000
    sum = 0
    for i in range(1000):
        sum = sum + delta * (fun(a+2*i*delta) + 4 * fun(a+(2*i+1)*delta)
         + fun(a+(2*i+2)*delta)) / 3.0
    return sum

# for term 1 in Z00
def three_dimension_number(x,y,z):
    return x*x + y*y + z*z

# for term 3 in Z00
def fun_3(t,q):
        return t**(-3/2)*np.exp(t*q)*(6*np.exp(-np.pi*np.pi/t)+
         12*np.exp(-2*np.pi*np.pi/t)+8*np.exp(-3*np.pi*np.pi/t)+6*np.exp(-4*np.pi*np.pi/t))

def Z00(q):
    term1 = np.exp(q) * np.sum([np.exp(-three_dimension_number(i,j,k)) / (three_dimension_number(i,j,k) - q)
     for k in range (-4,5) for j in range(-4,5) for i in range(-4,5)]) / (2*np.sqrt(np.pi))

    term2 = np.pi*np.sum([q**m/(np.math.factorial(m)*(m-1/2)) for m in range(1, 18)])/2
    
    def qfun_3(t):
        return fun_3(t,q)
    
    term3 = np.sqrt(np.pi) * integration(0.2,1,qfun_3) /2

    return term1 + term2 + term3 - np.pi

# solve the equation by binary search
def solve(f,left,right):
    if f(left) * f(right) > 0:
        print("error when binary search!")
        exit(1)

    if abs(left-right) < 1e-9:
        return left
    
    middle = (left + right) / 2.0

    if abs(f(middle)) < 1e-9:
        return middle
    elif f(left) * f(middle) < 0:
        return solve(f,left,middle)
    else:
        return solve(f,middle,right)

def fun(q):
    return Z00(q) - np.pi**(3/2)*(1+0.25*q)

ans = solve(fun,0.00001,0.99999)
print(ans)