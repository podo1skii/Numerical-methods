import math

delU = 0.00000067
delG = 0.00000071
delF = 0.00000033



def geron(w,u):
    return (w + u/w)/2


def f(x):
    return math.sqrt(2*x + 0.4)*math.atan(math.cos(3*x + 1))

def myf(x):
    cosin = 0
    result  = 0
    w = 1
    # print("-----Вычисляем корень-----")
    while (w - geron(w,2*x + 0.4)) > delU:
        w = geron(w,2*x + 0.4)
    # print("Приближенный корень: ", w)
    # print("-----Вычисляем косинус-----")
    k = 0
    while (math.pow(3*x + 1,2*k)/math.factorial(2*k)) > delG :
        cosin += math.pow(-1,k)*math.pow(3*x + 1,2*k)/math.factorial(2*k)
        k+=1


    # print("Приближенный косинус: ", cosin)
    # print("-----Вычисляем f-----")
    k = 0
    result = w*(math.pow(-1,k)*math.pow(cosin,2*k+1)/(2*k+1))
    k = k + 1
    while (w*(math.pow(cosin,2*k + 1)/(2*k + 1))) > delF:
        result += w*(math.pow(-1,k)*math.pow(cosin,2*k + 1)/(2*k + 1))
        k = k + 1
    result += w*(math.pow(-1,k)*math.pow(cosin,2*k + 1)/(2*k + 1))
    # print(result)
    return result

i = 0.01
print("x        python          with series")
while i<=0.06:
    print(round(i,3),"\t", round(f(round(i,3)),10),"\t", round(myf(round(i,3)),10))
    i = i + 0.005
