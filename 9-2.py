import numpy as np 
N=3

A = np.array([[1, 5, 1], [4, -1, 1], [1, 6, 20]])
B = np.array([19, 10, 354])


Adiag = np.diag(A)
Alpha = A.T/Adiag
Alpha[np.diag_indices_from(Alpha)] = 0
Alpha = Alpha.T

print('===================')
print(Alpha)
print('===================')

Beta = B/Adiag
print(Beta)
print('===================')

x = np.zeros(N, dtype = float)
z = 100
KMAX = 100
k = 0

while (z>0.001) & (k<KMAX):
    z = 0
    for i in range(0,N):
        y=x[i]
        x[i]= Beta[i] - np.dot(Alpha[i],x)
        z=z+abs(x[i]-y)
    k+=1

print("k = ", k, "Погрешность = ", z)
print('')
