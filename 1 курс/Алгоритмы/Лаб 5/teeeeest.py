import math

def f(x):
    return x**2 * math.exp(-abs(x))

def gausses(A, b):
    n = len(A)
    for i in range(n):
        max_el = abs(A[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > max_el:
                max_el = abs(A[k][i])
                max_row = k
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]
        
        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]
            b[k] += c * b[i]

    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = b[i] / A[i][i]
        for k in range(i - 1, -1, -1):
            b[k] -= A[k][i] * x[i]
    return x

def mnk(polynomial_degree, x):
    num_nodes = len(x)
    y = [f(xi) for xi in x]

    X = []
    for xi in x:
        row = [xi ** i for i in range(polynomial_degree + 1)]
        X.append(row)

    A = [[0] * (polynomial_degree + 1) for _ in range(polynomial_degree + 1)]
    for i in range(polynomial_degree + 1):
        for j in range(polynomial_degree + 1):
            A[i][j] = sum(X[k][i] * X[k][j] for k in range(num_nodes))

    b = [0] * (polynomial_degree + 1)
    for i in range(polynomial_degree + 1):
        b[i] = sum(X[k][i] * y[k] for k in range(num_nodes))

    coefficients = gausses(A, b)

    return coefficients

polynomial_degree = 3
x = [-1, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
coefficients = mnk(polynomial_degree, x)

print("Коэффициенты полинома:")
print(coefficients)
