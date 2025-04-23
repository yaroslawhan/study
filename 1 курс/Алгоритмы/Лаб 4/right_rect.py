def right_rect(f, mode, n, a, b, eps):
	if mode == 1:
		h = (b-a)/n
		summ = 0
		for i in range(1, n+1):
			summ += f(a+i*h)
		result = h*summ
		return result
	if mode == 2:
		x = n
		y = a
		eps = b
		summ = 0
		for i in range(1, len(x)):
			summ += (x[i]-x[i-1])*y[i]
		result = summ
		return result