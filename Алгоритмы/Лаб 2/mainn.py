from jacobi import jacobi

# Блок данных
eps = 0.001

# Системы в разных формах
def system_expr(x, y):
	return [(9*y-2*7/(7+1))**(1/4), (((x**2)*(y**2)-3*x**3+2*7)/6)**(1/3)]
	#return [(9*y-2*7/(7+1))**(1/4), ((3*x**3-2*7)/(x**2-6*y))**(1/2)]
def system_unexpr(x, y):
	return [(x**2)*(y**2) - 3*x**3 - 6*y**3 + 2*7, x**4 - 9*y + 2*(7/(7+1))]

print(jacobi(system_expr, system_unexpr, -2, 2, eps)) 