import numpy as np

A = np.zeros((10,10))

for i in range(10):
    for j in range(10):
        if(i==j):
            A[i,j] = 2
        elif((i-1) % 10 ==j):
            A[i,j] = -1
        elif((i+1) % 10 ==j):
            A[i,j] = -1
        else:
            A[i,j] = 0

print(A)

q0 = np.random.rand(10)
q1 = np.dot(A,q0) / np.linalg.norm(np.dot(A,q0))
diff = max(np.abs(q1 - q0))

while(diff>1e-10):
    z1 = np.dot(A,q0)
    q1 = z1 / np.linalg.norm(z1)
    v1 = np.dot(q1,np.dot(A,q1))
    diff = max(np.abs(q1 - q0))
    q0 = q1

print(q1)
print(v1)