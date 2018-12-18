import numpy as np
import copy

def norm(x):
    sum = 0
    for item in x:
        sum = sum+ item**2
    return np.sqrt(sum)

def P(A,k):
    n = A.shape[0]
    x = A[k:,k]
    w = copy.deepcopy(x)
    w[0] = w[0] - norm(x)
    nor = norm(w)**2

    w = np.array([w])
    W = np.dot(w.T,w) * 2 / nor
    R = np.eye(n-k) - W

    p = np.zeros((n,n))
    for i in range(k):
        p[i,i] = 1
    for m in range(k,n):
        for j in range(k,n):
            p[m,j] = R[m-k,j-k]
    
    return p

def HouseHolderQR(A):
    n = A.shape[0]
    Q = np.eye(n)
    R = copy.deepcopy(A)

    for i in range(n-1):
        p=P(R,i)
        R=np.dot(p,R)
        Q = np.dot(p,Q)
    
    return Q.T,R

# A = np.array(
#     [[1,4,2],
#     [1,5,3],
#     [2,4,7]],dtype=float
# )

# q,r = HouseHolderQR(A)
# Q,R = np.linalg.qr(A)

# print(q)
# print(Q)

# print(r)
# print(R)

# ans = np.dot(q,r)

# print(ans)