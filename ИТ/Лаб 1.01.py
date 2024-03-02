#Лабораторная работа №1-01

from math import *

x = 0.5
y = 0
a = atan(sqrt(3)/3) + log(abs((x+1)/(x-1)), 1/3)*cos(pi*x+pi/3)
b = ((e**y + e**(-y))/(1+(sin(y+pi/4))**2))*(1+((y-1)**2)/27)**(1/3)

print("a = %.3f"%a)
print("b = %.3f"%b)

x = float(input("Введите число x: "))
y = float(input("Введите число y: "))

a = atan(sqrt(3)/3) + log(abs((x+1)/(x-1)), 1/3)*cos(pi*x+pi/3)
b = ((e**y + e**(-y))/(1+(sin(y+pi/4))**2))*(1+((y-1)**2)/27)**(1/3)

if ((b - a) ** 2 + a * x + x ** 2) == 0:
    print("Решений нет")
else:
    if a>b:
        u = ((x + 1) * (2 * a + b * x) ** (3 / 2)) / ((b - a) ** 2 + a * x + x ** 2)
    else:
        u = ((x - 1) * (2 * b + a * x) ** (1 / 2)) / ((b - a) ** 2 + a * x + x ** 2)
    print("U = %.3f"%u)