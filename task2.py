A = [[5, 1, 1, 1],[1 ,6 ,1 ,1],[1 ,1 ,7 ,1],[1 ,1 ,1 ,8]]
b = [8,9,10,11]
A = [A[3],A[2],A[1],A[0]]
b = [b[3],b[2],b[1],b[0]]
x = [0,0,0,0]
def multArray(array, value):
    a = [0,0,0,0]
    for i in range(len(array)):
        a[i] += value*array[i]
    return a


def sumVectors(array1, array2):
    a = [0,0,0,0]
    for i in range(len(array1)):
        a[i] = array1[i] + array2[i]
    return a


def diffVectors(array1, array2):
    a = [0,0,0,0]
    for i in range(len(array1)):
        a[i] = array1[i] - array2[i]
    return a

for i in range(1,len(A)):
    b[i] = b[i] - b[0]*(A[i][0]/A[0][0])
    A[i] = diffVectors(A[i],multArray(A[0],A[i][0]/A[0][0]))



A = [A[0],A[2],A[3],A[1]]
b = [b[0],b[2],b[3],b[1]]

for i in range(2,len(A)):
    b[i] = b[i] - b[1]*(A[i][1]/A[1][1])
    A[i] = diffVectors(A[i],multArray(A[1],A[i][1]/A[1][1]))

for i in range(3,len(A)):
    b[i] = b[i] - b[2]*(A[i][2]/A[2][2])
    A[i] = diffVectors(A[i],multArray(A[2],A[i][2]/A[2][2]))

x[3] = b[3]/A[3][3];
x[2] = (b[2] - A[2][3]*x[3])/A[2][2]
x[1] = (b[1] - A[1][3]*x[3] - A[1][2]*x[2])/A[1][1]
x[0] = (b[0] - A[0][1]*x[1] - A[0][3]*x[3] - A[0][2]*x[2])/A[0][0]

print("------Проверка------")
print(x[0]+x[1]+x[2]+x[3]*8)
print(x[0]+x[1]+x[2]*7+x[3])
print(x[0]+x[1]*6+x[2]+x[3])
print(x[0]*5+x[1]+x[2]+x[3])
print("--------------------")
print("X =",x)
