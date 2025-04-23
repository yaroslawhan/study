# Метод касательных(Ньютона)
from sympy import *

def tangent(a, b, eps, x1, y, f):
    if f(a)*f(b) < 0:
        x = (a+b)/2
        count = 1
        xl = [x]
        while (abs(f(x))) >= eps:
            x = x - (f(x))/(diff(y).subs(x1, x))
            xl.append(x)
            count += 1
        return x, xl, count
    else:
        return "Корней нет"