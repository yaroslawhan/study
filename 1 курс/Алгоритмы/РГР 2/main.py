from tkinter import *
from math import *
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scripts import *

win = Tk()
win.title('ДЗ №2, Ханевский, АС-23-04, вар. 26')
win.geometry('900x550')
win.config(bg="white")

img1 = PhotoImage(file='img_1.png')
Label(win, image=img1).place(x=10, y=20)
img2 = PhotoImage(file='img_2.png')
Label(win, image=img2).place(x=10, y=360)
img3 = PhotoImage(file='img_3.png')
Label(win, image=img3).place(x=505, y=20)

# ЗАДАНИЕ 1

eps = 0.001

# Вывод текста 
Label(win, text="Введите левую границу графика:", font='Times 14', bg="white").place(x=10, y=50)
Label(win, text="Введите правую границу графика:", font='Times 14', bg="white").place(x=10, y=80)
Label(win, text="Введите левую границу локализ-и:", font='Times 14', bg="white").place(x=10, y=110)
Label(win, text="Введите правую границу локализ-и:", font='Times 14', bg="white").place(x=10, y=140)
Label(win, text='X =', font=("Times New Roman", 14), bg="white").place(x=10, y=220)
Label(win, text='Число итераций =', font=("Times New Roman", 14), bg="white").place(x=10, y=280)
Label(win, text='Y =', font=("Times New Roman", 14), bg="white").place(x=10, y=250)

# Ввод
A = Entry(bg='white')
A.place(x=305, y=55)
B = Entry(bg='white')
B.place(x=305, y=85)
a1 = Entry(win, bg='white')
a1.place(x=305, y=115)
b1 = Entry(win, bg='white')
b1.place(x=305, y=145)

# Функция
def f1(x):
    return (x**3 - 12*x - 10)

# Вывод графика
def graphic():
    a = float(A.get())
    b = float(B.get())
    fig, ax = plt.subplots(figsize=(6, 4))
    x = np.linspace(a, b, 100)
    y = x ** 3 - 12 * x - 10
    ax.plot(x, y)
    ax.grid(True)
    ax.set_xlabel('Ось X', fontsize=10)
    ax.set_ylabel('Ось Y', fontsize=10)
    ax.axhline(y=0, color='g')
    ax.axvline(x=0, color='g')
    ax.set_title('y = x**3 - 12*x - 10')
    plt.show()

# Комбинированный метод
def Combined():
    right = float(b1.get())
    left = float(a1.get())
    print(right)
    script = NonLinearEquationSolve(left, right, eps)
    print(1)
    Label(text=str(script.chords_and_tangents()[3]), font='Times 14', bg="white").place(x=160, y=280)
    Label(text=str(round(script.chords_and_tangents()[0], 3)), font='Times 14', bg="white").place(x=50, y=220)
    Label(text=str(round(f1(script.chords_and_tangents()[0]), 3)), font='Times 14', bg="white").place(x=50, y=250)

# Вывод кнопок
Button(text='Рассчитать корень', font=("Times New Roman", 14), command=Combined).place(x=10, y=180)
Button(text='Построить график', font=("Times New Roman", 14), command=graphic).place(x=200, y=180)

# ЗАДАНИЕ 2

# Вывод текста
Label(text='Приближенное значение интеграла:', font='Times 14', bg="white").place(x=10, y=480)
Label(text='Число разбиений:', font='Times 14', bg="white").place(x=10, y=510)

def f2(x):
    return ((1+(0.8)*x**2)/(1.5+((0.4)*x**2+1)**(1/2)))

def tri8(a, b, n):
    h = (b - a) / n
    summ = f2(a) + f2(b)
    for i in range(1, n):
        x = a + i * h
        if i % 3 == 0:
            summ += 2 * f2(x)
        else:
            summ += 3 * f2(x)
    return (3 * h / 8) * summ

def tri_vosem(three_eighths_rule=None):
    n1 = 9
    n2 = 12
    I1 = tri8(0.8, 2.6, n1)
    I2 = tri8(0.8, 2.6, n2)
    while abs(I2 - I1) > eps:
        n1 = n2
        I1 = I2
        n2 += 3
        I2 = three_eighths_rule(1.4, 2.84, n2)
    Label(text=str(round(I2, 4)), font='Times 14', bg="white").place(x=310, y=480)
    Label(text=str(n2), font='Times 14', bg="white").place(x=160, y=510)

# Вывод кнопки
Button(text='Вычислить интеграл', font=("Times New Roman", 14), command=tri_vosem).place(x=10, y=430)

# ЗАДАНИЕ 3
def f3(x, y):
    return (0.273*(x**2+cos((1.3)*x))+(0.687)*y)

X = []
h = 0.1
n = 11
for i in range(2, 13, 1):
    X.append(i / 10)
f01 = [1 / 4]

def Euler_fun(f0):
    for i in range(n):
        f0.append(f0[i] + h * f3((X[i] + h / 2), (f0[i] + h * 0.5 * f3(X[i], f0[i]))))
    return f0

def Euler():
    z = Euler_fun(f01)
    Label(text='X', font=("Times New Roman", 14), width=5, bg='white').place(x=505, y=105)
    Label(text='Y', font=("Times New Roman", 14), width=5, bg='white').place(x=580, y=105)
    for i in range(len(X)):
        Label(text=str(X[i]), font=("Times New Roman", 14), width=5, bg='white').place(x=505, y=135 + 20 * i)
        Label(text=str(round(z[i], 4)), font=("Times New Roman", 14), width=10, bg='white').place(x=555, y=135 + 20 * i)

# Вывод кнопки
Button(text='Усовершенствованный метод ломаных', font=("Times New Roman", 14), command=Euler).place(x=505, y=65)

win.mainloop()