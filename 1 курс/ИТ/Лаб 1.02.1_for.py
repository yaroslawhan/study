#Лабораторная работа №1-02

#1
from math import *
import matplotlib.pyplot as plt
import matplotlib

b = -1.28
c = 0.16
x_data = []
y_data = []
table_data = []

print("a z")

for i in range(-10, 41, 5):
    a = i/10
    d = b**2 - 4*a*c
    if d < 0:
        x_data.append(a)
        y_data.append(None)
        table_data.append([a, "Решений нет"])
        print(a, "Решений нет")
        continue
    else:
        x1 = (-b + sqrt(d))/2*a
        x2 = (-b - sqrt(d))/2*a
        x = max(x1, x2)
        if x == a:
            x_data.append(a)
            y_data.append(None)
            table_data.append([a, "Решений нет"])
            print(a, "Решений нет")
            continue
        z = sqrt((log(abs(1+x)))/abs(tan(x/2))) + sqrt(abs(x) + e**(3*x))
        x_data.append(a)
        y_data.append(z)
        table_data.append([a, "%.3f"%z])
        print(a, "%.3f"%z)

#график
plt.figure('График')
plt.title('График функции y=sqrt((log(abs(1+x)))/abs(tan(x/2))) + sqrt(abs(x) + e**(3*x))', fontsize=13, fontname='Times New Roman')
plt.plot(x_data, y_data, c = 'red', marker='*') #График точками
plt.grid('on')
plt.plot(x_data, y_data, c = 'green') #График линией в том же окне

#таблица
plt.figure('Таблица')
plt.title('Таблица значений функции y=sqrt((log(abs(1+x)))/abs(tan(x/2))) + sqrt(abs(x) + e**(3*x))', fontsize=12, fontname='Times New Roman')
plt.table(cellText=table_data, loc='center', colLabels = ['x', 'y'], bbox=[0, 0, 1, 1])
plt.axis('off') #Выключаем координатную сетку
plt.show() #Вывести графики на экра