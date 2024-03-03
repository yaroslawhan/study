# Метод итераций

def iteration(a, b, eps, f, f1):
	if f(a)*f(b) < 0:
		x = (a+b)/2
		xl = [x]
		count = 1
		approach = []
		while (abs(f(x))) >= eps:
			approach.append(x-f1(x))
			x = f1(x)
			xl.append(x)
			count += 1
			if len(approach) > 1:
				if approach[-1] >= approach[-2]:
					return "Ряд не сходится"
		return x, xl, count
	else:
		return "Корней нет"