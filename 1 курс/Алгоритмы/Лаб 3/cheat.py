import tkinter as tk
from tkinter import font
import copy

def gauss_elimination(A, B):
    n = len(A)
    A = copy.deepcopy(A)  # Создаем копию матрицы A
    B = copy.deepcopy(B)  # Создаем копию вектора B
    # Прямой ход
    for i in range(n):
        # Поиск главного элемента в текущем столбце
        max_row = i
        for k in range(i+1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
                
        # Перестановка строк, если необходимо
        A[i], A[max_row] = A[max_row], A[i]
        B[i], B[max_row] = B[max_row], B[i]
        
        # Приведение матрицы к треугольному виду
        for k in range(i+1, n):
            factor = A[k][i] / A[i][i]
            B[k] -= factor * B[i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
                
    # Обратный ход
    X = [0] * n
    for i in range(n-1, -1, -1):
        X[i] = B[i] / A[i][i]
        for k in range(i-1, -1, -1):
            B[k] -= A[k][i] * X[i]
            
    return X

def gauss_jordan_elimination(A, B):
    n = len(A)
    A = copy.deepcopy(A)  # Создаем копию матрицы A
    B = copy.deepcopy(B)  # Создаем копию вектора B
    
    # Прямой ход
    for i in range(n):
        # Поиск главного элемента в текущем столбце
        max_row = i
        for k in range(i+1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
                
        # Перестановка строк, если необходимо
        A[i], A[max_row] = A[max_row], A[i]
        B[i], B[max_row] = B[max_row], B[i]
        
        # Приведение матрицы к треугольному виду
        pivot = A[i][i]
        for j in range(i, n):
            A[i][j] /= pivot
        B[i] /= pivot
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(i, n):
                    A[k][j] -= factor * A[i][j]
                B[k] -= factor * B[i]
    
    # Обратный ход
    X = [0] * n
    for i in range(n):
        X[i] = B[i]
    
    return X

def solve_gauss():
    global A, B, gauss_result, gauss_jordan_result
    gauss_result = gauss_elimination(A, copy.deepcopy(B))  # Создаем копию вектора B
    result_label_gauss.config(text=format_results(gauss_result))
    save_results()

def solve_gauss_jordan():
    global A, B, gauss_result, gauss_jordan_result
    gauss_jordan_result = gauss_jordan_elimination(A, copy.deepcopy(B))  # Создаем копию вектора B
    result_label_gauss_jordan.config(text=format_results(gauss_jordan_result))
    save_results()

def format_results(results):
    if results is None:
        return ""
    else:
        formatted_results = "\n".join([f"{result:.3f}" for result in results])
        return formatted_results

def save_results():
    with open("results.txt", "w", encoding="utf-8") as f:
        f.write("Метод Гаусса:\n")
        f.write(format_results(gauss_result))
        f.write("\n\n")
        f.write("Метод Гаусса-Жордана:\n")
        f.write(format_results(gauss_jordan_result))

# Создание окна
root = tk.Tk()
root.title("Лабораторная работа 3")
root.geometry("1280x720")

# Шрифт Arial размера 12
font_style = font.Font(family="Arial", size=12)

# Создание рамки для вывода системы уравнений
equations_frame = tk.Frame(root)
equations_frame.pack(padx=10, pady=10)

# Создание текстовых меток и вывод уравнений
equations = [
    "7.6*X + 5.8*Y + 4.7*Z = 10.1",
    "3.8*X + 4.1*Y + 2.7*Z = 9.7",
    "2.9*X + 2.1*Y + 3.8*Z = 7.8"
]
for i, equation in enumerate(equations):
    tk.Label(equations_frame, text=equation, font=font_style).grid(row=i, column=0)

# Кнопка для решения методом Гаусса
gauss_button = tk.Button(root, text="Решить методом Гаусса", command=solve_gauss, font=font_style)
gauss_button.pack(pady=10)

# Место для вывода результата метода Гаусса
result_label_gauss = tk.Label(root, text="", font=font_style)
result_label_gauss.pack()

# Кнопка для решения методом Гаусса-Жордана
gauss_jordan_button = tk.Button(root, text="Решить методом Гаусса-Жордана", command=solve_gauss_jordan, font=font_style)
gauss_jordan_button.pack(pady=10)

# Место для вывода результата метода Гаусса-Жордана
result_label_gauss_jordan = tk.Label(root, text="", font=font_style)
result_label_gauss_jordan.pack()

# Матрица коэффициентов и вектор правой части
A = [[7.6, 5.8, 4.7],
     [3.8, 4.1, 2.7],
     [2.9, 2.1, 3.8]]

B = [10.1, 9.7, 7.8]

# Переменные для хранения результатов
gauss_result = None
gauss_jordan_result = None

root.mainloop()