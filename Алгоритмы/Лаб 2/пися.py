def jacobi(system_expr, system_unexpr, x0, y0, eps):
    x = x0
    y = y0
    while True:
        x_new = system_expr(x, y)[0]
        y_new = system_expr(x, y)[1]
        if abs(x_new - x) < eps and abs(y_new - y) < eps:
            break
        x = x_new
        y = y_new

    return [x_new, y_new]

# Блок данных
eps = 0.001

# Системы в разных формах
def system_expr(x, y):
    return [((9*y-2*7/(7+1))**(1/4)), (((x**2)*(y**2)-3*x**3+2*7)/6)**(1/3)]

def system_unexpr(x, y):
    return [(x**2)*(y**2) - 3*x**3 - 6*y**3 + 2*7, x**4 - 9*y + 2*(7/(7+1))]

print(jacobi(system_expr, system_unexpr, -2, 2, eps))
