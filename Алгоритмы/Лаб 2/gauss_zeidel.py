def gauss_zeidel(system_expr, system_unexpr, x0, y0, eps):
	x = x0
	y = y0
	count = 0
	while abs(system_unexpr(x, y)[0]) > eps or abs(system_unexpr(x, y)[1]) > eps:
		if count > 500:
			return ["Корней нет", "Корней нет", 0]
		count += 1
		temp = system_expr(x, y)
		print(temp)
		x = system_expr(temp[0], temp[1])[0]
		y = system_expr(x, temp[1])[1]

	return [x, y, count]