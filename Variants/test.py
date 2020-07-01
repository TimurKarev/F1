import numpy as np

number = 9
d = np.ones((number+1,number+1), dtype=int) * -1

def dec(n, k):
    if(n >= 0 and k >=0 and d[n][k] > 0):
        print("F")
        print("n=" + str(n) + " k=" + str(k) + " d[][]=" + str(d[n][k]))
        return d[n][k]
    if(n < 0 ):
        print("S")
        print("n=" + str(n) + " k=" + str(k) + " d[][]=" + str(d[n][k]))
        return 0
    if (n <= 1 or k == 1):
        print("T")
        print("n=" + str(n) + " k=" + str(k) + " d[][]=" + str(d[n][k]))
        return 1
    print("NN")
    print("n=" + str(n) + " k=" + str(k) + " d[][]=" + str(d[n][k]))
    d[n][k] = dec(n,k-1) + dec(n-k, k)
    
    return d[n][k]


print("n: " + str(number) + " = " + str(dec(number, number)))
print(d)


