def simpson(f, mode, n, a, b, eps):
	if mode == 1:
		h = (b-a)/n
		result = f(a) + f(b)
		for i in range(1, n):
			if i%2 == 0:
				result += 2*f(a+i*h)
			else:
				result += 4*f(a+i*h)
		result *= h/3
		return result
	if mode == 2:
		x = n
		y = a
		eps = b
		result = y[0] + y[-1]
		h = (x[-1]-x[0])/((len(x)-1))
		for i in range(1, len(x)-1):
			if i%2 == 0:
				result += 2*y[i]
			else:
				result += 4*y[i]
		result *= h/3
		return result