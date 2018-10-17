#python 3
import math
#import numpy as np

# create a matrix with 0.0 as intial value, which has n rows and m cols
def zeros(n,m):
    zeros = []
    for i in range(n):
        line = []
        for j in range(m):
            line.append(0.0)
        zeros.append(line)
    return zeros

# create a 1d vector with 0.0 as initial value, which has n terms
def zeros_1d(n):
    zeros = []
    for i in range(n):
        zeros.append(0.0)
    return zeros

# input two 2d matrixs, ouput the multiply result
def multip(A,B):
    if len(A[0]) != len(B):
        print("cannot multiply A by B!")
        exit(1)

    n = len(B)    
    rows = len(A)
    cols = len(B[0])
    result = zeros(rows,cols)

    for i in range(rows):
        for j in range(cols):
            for k in range(n):
                result[i][j] = result[i][j] + A[i][k] * B[k][j]

    return result

# input two 1d vectors, output the scalar by multiplying each corresponding index
def dot(A,B):
    # they should have same rows
    if len(A) != len(B):
        print("cannot dot A and B!")
        exit(1)

    if len(A) == 0:
        return 0.0
    
    result=0.0
    for i in range(len(A)):
        result = result+ A[i] * B[i]
    
    return result

# A is the matrix and b is the vector. Solve the equation using GEM method.
def GEM(A,b):
    #rows = A.shape[0]
    rows = len(A)
    if rows != len(b):
        print("incompatible matrix A and b")
        exit(1)

    for i in range(0,rows-1):
        # select the pivot by the max
        firstcol=[]
        for ii in range(i,rows):
            firstcol.append(A[ii][i])

        pivot = firstcol.index(max(firstcol)) + i
        #A[[i,pivot],:] = A[[pivot,i],:]

        #exchange rows
        c = A[i]
        A[i] = A[pivot]
        A[pivot] = c
        b[i],b[pivot] = b[pivot],b[i]
        
        for j in range(i+1,rows):
            if A[j][i]!=0.0:
                fro = A[j][i] / A[i][i]
                A[j][i] = 0.0
                #A[j][i+1:rows] = - fro * A[i][i+1:rows] + A[j][i+1:rows]
                for k in range(i+1,rows):
                    A[j][k] = -fro * A[i][k] + A[j][k]
                b[j] = - fro * b[i] + b[j]
    
    x = zeros_1d(rows)

    for k in range(rows-1,-1,-1):
        x[k] = (b[k] - dot(A[k][k+1:rows],x[k+1:rows]))/A[k][k]
    
    return x

# A is the matrix and b is the vector. Solve the equation using choleskey method.
def choleskey(A,b):
    rows = len(A)
    cols = len(A[0])
    if rows != len(b):
        print("incompatible matrix A and b")
        exit(0)
    if rows != cols:
        print("not correct matirx!")
        exit(0)

    H = zeros(rows,cols)

    H[0][0] = math.sqrt(A[0][0])
    for i in range(1,rows):
        for j in range (0,i):
            H[i][j] = (A[i][j] - dot(H[i][0:j],H[j][0:j]))/H[j][j]
        H[i][i] = math.sqrt(A[i][i] - dot(H[i][0:i],H[i][0:i]))
    
    x1 = zeros_1d(rows)
    x2 = zeros_1d(cols)

    for m in range(rows):
        x1[m] = (b[m] - dot(H[m][0:m],x1[0:m]))/H[m][m]
    
    #x2[rows-1] = x1[rows-1] / H[rows-1][rows-1]
    for n in range(rows-1,-1,-1):
        h_inv = [x[n] for x in H[n+1:rows]]
        #x2[n] = (x1[n] - dot(H[n+1:rows][n],x2[n+1:rows]))/H[n][n]
        x2[n] = (x1[n] - dot(h_inv,x2[n+1:rows]))/H[n][n]
    
    return x2

#create a n dimension hilbert matrix
def create_hilbert(n):
    mat = []
    for i in range(1,n+1):
        line = []
        for j in range(1,n+1):
            h = 1.0 / (i+j-1)
            line.append(h)
        mat.append(line)
    #hilbert = np.array(mat)
    return mat

# create a sample ouput, which has 1.0 as initial value.
def create_vector(n):
    #return np.array([1 for i in range (1,n+1)],dtype=np.float)
    vec= []
    for i in range(n):
        vec.append(1.0)
    return vec


file1 = open(r'HW_1_source_code/GEM1.txt','w')
file2 = open(r'HW_1_source_code/Choleskey1.txt','w')

for n in range (1,13):
    A1 = create_hilbert(n)
    b1 = create_vector(n)
    A2 = create_hilbert(n)
    b2 = create_vector(n)

    result_1 = GEM(A1,b1)
    result_2 = choleskey(A2,b2)
    string = "n = {} \n".format(n)

    file1.write(string)
    r1 = str(result_1) + "\n \n"
    file1.write(str(r1))

    file2.write(string)
    r2 = str(result_2) + "\n \n"
    file2.write(str(r2))

file1.close()
file2.close()