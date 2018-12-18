import numpy as np
import copy

def Givens(A,i,j):
    n = A.shape[0]
    G = np.eye(n)
    x1 = A[i,i]
    x2 = A[j,i]
    c = x1 / np.sqrt(x1**2+x2**2)
    s = x2 / np.sqrt(x1**2+x2**2)
    G[i,i] = c
    G[i,j] = s
    G[j,i] = -s
    G[j,j] = c

    return G

def GivensQR(A):
    n = A.shape[0]
    Q = np.eye(n)
    R = copy.deepcopy(A)

    for i in range(n-1):
        for j in range(i+1,n):
            G = Givens(R,i,j)
            R = np.dot(G,R)
            Q = np.dot(G,Q)
    
    return Q.T,R


# A=np.array(
#     [[1,2,3],
#      [1,3,4],
#      [1,5,7]],dtype=float
# )

# q,r = GivensQR(A)
# Q,R = np.linalg.qr(A)


# print(q)
# print(Q)

# print(r)
# print(R)

# ans = np.dot(q,r)

# print(ans)