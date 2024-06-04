#библиотека для параметризации функции и построения графиков
from sympy import *

#для построения набора точек на графике
import matplotlib.pyplot as plt

#для решения СЛАУ
import Gaussa
import numpy
from math import *

x = symbols('x')
K = 3 #степень многочлена
a = -1
b = 3
n = 8
dx = (b-a)/n

# Исходная функция
def f(x):
    return x**2 * e**((-1)*abs(x))

#опорные точки
xi = []
yi = []
i = a
while i <= b:
    xi.append(i)
    yi.append(f(i))
    i += dx

def approksim(xi, yi, K):
    #поиск констант
    A = numpy.zeros([K + 1, K + 1])
    for i in range(K + 1):
        for j in range(K + 1):
            for t in xi: A[i, j] += t ** (2 * K - i - j)
    a = numpy.zeros([K + 1])
    for i in range(K + 1):
        for j in range(len(xi)): a[i] += yi[j] * xi[j] ** (K - i)
    const = []
    for j in Gaussa.Metod_Gaussa(A, a): const.append(float(j))
    #составление уравнения
    f = 0
    for i in range(len(const)):
        f += const[i] * x ** (len(const) - 1 - i)
    return f

#значения линейной функции, полученной МНК, в тех же точках
f1 = []
for i in xi: f1.append(approksim(xi, yi, 1).evalf(subs={'x': i}))
#отклонения (невязки в точках)
e1 = []
for i in range(len(xi)): e1.append(abs(f1[i] - yi[i]))

#значения квадратичной функции, полученной МНК, в тех же точках
f2 = []
for i in xi: f2.append(approksim(xi, yi, 2).evalf(subs={'x': i}))
#отклонения (невязки в точках)
e2 = []
for i in range(len(xi)): e2.append(abs(f2[i] - yi[i]))

#значения кубической функции, полученной МНК, в тех же точках
f3 = []
for i in xi: f3.append(approksim(xi, yi, 3).evalf(subs={'x': i}))
#отклонения (невязки в точках)
e3 = []
for i in range(len(xi)): e3.append(abs(f3[i] - yi[i]))

#все функции на одном графике
xfi = numpy.linspace(xi[0], xi[len(xi) - 1], 100)
# f1i = [approksim(xi, yi, 2).subs(x, a) for a in xfi]
# f2i = [approksim(xi, yi, 3).subs(x, a) for a in xfi]
f3i = [approksim(xi, yi, 5).subs(x, a) for a in xfi]

print()

# plt.plot(xfi, f1i, 'b')
# plt.plot(xfi, f2i, 'r')
plt.plot(xfi, f3i, 'g')
plt.plot(xi, yi, 'k*')
plt.grid()
plt.show()