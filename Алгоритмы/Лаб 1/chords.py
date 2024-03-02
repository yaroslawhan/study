# Метод хорд
from sympy import *

def chords(a, b, eps, x1, y, f):
    if not(abs(diff(y).subs(x1, a)) < 1 and abs(diff(y).subs(x1, b)) < 1):
        return "Ряд не сходится"
    if f(a)*f(b) < 0:
        count = 1
        x = a - ((b-a)*(f(a)))/(f(b)-f(a))
        xl = [x]
        while (abs(f(x)) >= eps):
            if f(a)*f(x) < 0:
                b = x
            else:
                a = x
                
            x = a - ((b-a)*(f(a)))/(f(b)-f(a))
            count += 1
            xl.append(x)
        return x, xl, count
    else:
        return "Корней нет"