import math




def f(x):
    return math.pow(x,2)-math.acos(x)+1

def fderiv(x):
    return 2*x+1/(math.sqrt(1 - math.pow(x,2)))


def newton(x):
    return x - f(x)/fderiv(x)

x0 = 0.8
t = 100
# print(math.pow(0.8,2)-math.acos(0.8)+1)
# print((math.sqrt(1 - math.pow(0,2))))
while t > 0.0001:
    print(x0)
    print(f(x0))
    xk = x0 - f(x0)/fderiv(x0)
    t = abs(x0 - xk)
    x0 = xk

print(x0)
