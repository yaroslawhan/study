# Метод итераций
from sympy import *

def iteration(a, b, eps, x1, y, f):
	if abs(diff(y)) >= 0:
		return "Ряд не сходится"
	if f(a)*f(b) < 0:
		x = (a+b)/2
		xl = [x]
		count = 1
		while (abs(f(x))) >= eps:
			x = f1(x)
			xl.append(x)
			count += 1
		return x, xl, count
	else:
		return "Корней нет"