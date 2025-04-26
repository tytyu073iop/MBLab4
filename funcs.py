import math

def func(x):
    return math.log(1 + x)/(1 + x ** 2)

def trap(a, b, h, n):
    sum = 0
    for i in range(1 ,n):
        sum += func(a + h * i)
    return h * ((func(a) + func(b)) / 2 + sum)

def simpson(a, b, h, n):
    sum = 0
    for i in range(n):
        sum += func(a + h * i) + 4 * func(a + (h * i) + (h / 2)) + func(a + h * (i + 1))
    return (h / 6) * sum