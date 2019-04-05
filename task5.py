import math

eps = 0.0001

def hn(x , y):
    return (math.cos(y)+x - 1.5- 2*y + math.sin(x - 0.5)+1)/(-math.cos(x - 0.5)*math.sin(y)+2)


def gn(x,y):
    return math.sin(y)*hn(x,y) - math.cos(y) - x + 1.5


x = 0
y = 0
xk = 0
yk = 0
while math.sqrt(math.pow(hn(x,y),2)+math.pow(gn(x,y),2)) > eps:
    xk = x + gn(x,y)
    yk = y + hn(x,y)
    x = xk
    y = yk


print (x, y)
