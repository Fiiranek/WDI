# problem
# solve the equation x^x = 2020
# 1. Let's say that f(x) = x^x - 2020
# 2. Calculate derivative of f(x), so df(x) = x^x * (log(x) + 1)
# The problem is that during calculating potential x, our number can be too large for Python
# To omit it - we use log()
# 3. New f(x) = x*log(x) - log(2020)
# 4. New df(x) = log(x) + 1
import math


def f(x):
    return x* math.log(x) - math.log(2020)

def df(x):
    return math.log(x) + 1

def sol_17():
    x = 1
    eps = 0.0001
    while abs(f(x)) > eps:
        x = x - f(x)/df(x)
    return x
print(sol_17())