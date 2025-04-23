def trap(f, mode, n, a, b, eps):
	if mode == 1:
		h = (b-a)/n
		result = 0
		for i in range(n):
			result += 0.5*h*(f(a+i*h)+f(a+(i+1)*h))
		return result
	if mode == 2:
		x = n
		y = a
		eps = b
		result = 0
		h = (x[-1]-x[0])/((len(x)-1))
		for i in range(len(x)-1):
			result += 0.5*(y[i]+y[i+1])*(x[i+1]-x[i])
		return result