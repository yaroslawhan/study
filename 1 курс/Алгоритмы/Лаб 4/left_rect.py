def left_rect(f, mode, n, a, b, eps):
	if mode == 1:
		h = (b-a)/n
		summ = 0
		for i in range(n):
			summ += f(a+i*h)
		result = h*summ
		return result
	if mode == 2:
		x = n
		y = a
		eps = b
		summ = 0
		for i in range(len(x)-1):
			summ += (x[i+1]-x[i])*y[i]
		result = summ
		return result