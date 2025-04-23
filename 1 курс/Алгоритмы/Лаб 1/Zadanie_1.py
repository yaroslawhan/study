from sympy import *

# Метод дихотомии

a = -5 #int(input("Введите число a: "))
b = -2 #int(input("Введите число b: "))
eps = 0.01 #int(input("Введите число eps: "))

def f(x):
    return (x**3 - 6*x + 2)

if f(a)*f(b) < 0:
    x = (a+b)/2
    while abs(f(x)) > eps:
        x = (a+b)/2
        if abs(f(x)) == 0:
            break
        if f(a)*f(x) < 0:
            b = x
        elif f(b)*f(x) < 0:
            a = x
print(x)

# Метод хорд
a = -5 #int(input("Введите число a: "))
b = -2 #int(input("Введите число b: "))
eps = 0.01 #int(input("Введите число eps: "))


y = x**3 - 6*x + 2

if f(a)*f(b) < 0:
    x = a - ((b-a)*(f(a)))/(f(b)-f(a))
    while abs(b-a) > eps:
        if f(b)*(diff(diff(f(x)).subs(x, x)).subs(x, x)) > 0:
            x = x - ((b-x)*(f(x)))/(f(b)-f(x))
        elif f(a)*(diff(diff(f(x)).subs(x, x)).subs(x, x)) > 0:
            x = a - ((x-a)*(f(x)))/(f(x)-f(a))

print(x)

# Метод касательных(Ньютона)
a = -5 #int(input("Введите число a: "))
b = -2 #int(input("Введите число b: "))
eps = 0.01 #int(input("Введите число eps: "))

a1, b1 = symbols("a1 b1")

