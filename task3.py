import numpy as np
import math
A = np.array([[8, 1, 1, 1], [1, 9, 1, 1], [1, 1, 10, 1], [1, 1, 1, 11]])
b = np.array([11, 12, 13, 14])

def mvmult(M, b):
    b1 = np.zeros(len(b))
    for i in range(len(b)):
        b1 += M[:, i]*b[i]
    return b1

def mmult(M, N):
    K1 = np.zeros((len(M), len(M)))
    for i in range(len(M)):
        K1[:, i] = mvmult(M, N[:, i])
    return K1


def ln(a):
    rez = 0
    for i in range(len(a)):
        rez += a[i]**2
    return (math.sqrt(rez))

def vmult(a, b):
    ab = np.zeros((len(a), len(a)))
    for i in range(len(a)):
        for j in range(len(a)):
            ab[i, j] = a[j]*b[i]
    return ab

#c = np.array([0.8165, 0.4082, 0.4082])
#print(vmult(c, c))

for i in range(len(A)):
    e = np.zeros(len(A) - i)
    e[0] = 1
    y = A[i:, i]
    alpha = ln(y)/ln(e)
    w = y + alpha*e
    w = w/ln(w)
    U = np.eye(len(w)) - 2*vmult(w, w)
    Z = np.eye(len(A))
    Z[i:, i:] = U
    A = mmult(Z, A)
    b = mvmult(Z, b)

x4 = b[3]/A[3, 3]
x3 = (b[2] - x4*A[2, 3])/A[2, 2]
x2 = (b[1] - x4*A[1, 3] - x3*A[1, 2])/A[1, 1]
x1 = (b[0] - x4*A[0, 3] - x3*A[0, 2] - x2*A[0, 1])/A[0, 0]
x = [x1, x2, x3, x4]

print (x)
