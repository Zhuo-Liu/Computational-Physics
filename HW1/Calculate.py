import math

def det(n):
    sum1 = 0
    sum2 = 0
    for i in range(1,n):
        sum1 = sum1 + (n-i)*math.log(i)
    for i in range(1,2*n):
        sum2 = sum2 + (2*n-i)*math.log(i)
    
    sum = 4.0 * sum1 - sum2
    det = math.exp(sum)
    return det

file1 = open(r'HW_1_source_code/det.txt','w')
for i in range(1,11):
    de = det(i)
    string = "|{}|".format(i)
    s = str(de)
    file1.write(string)
    file1.write(s)
    file1.write("| \n")

file1.close()