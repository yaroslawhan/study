from math import *
from matplotlib.pyplot import *
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy import interpolate
import numpy as np

# Блок данных
a = -1
b = 3
n = 8
dx = (b-a)/n

# Исходная функция
def f(x):
	return x**2 * e**((-1)*abs(x))

#Функция для окна
def lbl(t, xx, yy):
    l = Label(win, text=t, font=("Arial", 14), bg="white")
    l.place(x=xx, y=yy)

# Метод Гаусса
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

# МНК
# def mnk(degree, n):
# 	count_x = 2*degree
# 	count_y = 1 + degree
# 	kefs_x = []
# 	kefs_y = []
# 	a = []
# 	b = []
# 	k = 0
# 	for i in range(count_x):
# 		temp = 0
# 		for j in range(n):
# 			temp += (x[j])**(i+1)
# 		kefs_x.append(temp)
# 	for i in range(count_y):
# 		temp = 0
# 		for j in range(n):
# 			temp += (y[j])*(x[j])**(i)
# 		kefs_y.append(temp)

# 	temp = [n]
# 	for i in range(degree):
# 		temp.append(kefs_x[i])
# 	b.append(kefs_y[0])
# 	a.append(temp)

# 	for i in range(1, len(kefs_y)):
# 		temp = []
# 		for j in range(k, degree+k+1):
# 			temp.append(kefs_x[j])
# 		b.append(kefs_y[i])
# 		a.append(temp)
# 		k += 1
# 	return a, b

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
	
x = []
y = []
yf = []
i = a
while i <= b:
	x.append(i)
	y.append(f(i))
	i += dx
i = a
while i <= b:
	yf.append(f(i))
	i += 0.1

# Отрисовка окна
win = Tk()
win.geometry("1800x820")
win.configure(background="white")
win.title("Ханевский, АС-23-04, вар.26")

# Подсчёт коэффициентов полиномов
kefs_2 = mnk(2, x)#gausses(mnk(2, n)[0], mnk(2, n)[1])
kefs_3 = mnk(3, x)#gausses(mnk(3, n)[0], mnk(3, n)[1])
kefs_4 = mnk(4, x)#gausses(mnk(4, n)[0], mnk(4, n)[1])
kefs_5 = mnk(5, x)#gausses(mnk(5, n)[0], mnk(5, n)[1])

# Построение графика
y2 = []
y3 = []
y4 = []
y5 = []
temp = 0
xx = [i/10 for i in range(-10, 31)]
for i in range(len(xx)):
	temp = 0
	for j in range(len(kefs_2)):
		temp += kefs_2[j]*xx[i]**j
	y2.append(temp)
	temp = 0
	for j in range(len(kefs_3)):
		temp += kefs_3[j]*xx[i]**j
	y3.append(temp)
	temp = 0
	for j in range(len(kefs_4)):
		temp += kefs_4[j]*xx[i]**j
	y4.append(temp)
	temp = 0
	for j in range(len(kefs_5)):
		temp += kefs_5[j]*xx[i]**j
	y5.append(temp)

fig1 = Figure(figsize = (9, 9))
plot1 = fig1.add_subplot(221)
plot1.scatter(x, y, color="purple")
plot1.plot(xx, y2, color="red")
plot2 = fig1.add_subplot(222)
plot2.scatter(x, y, color="purple")
plot2.plot(xx, y3, color="black")
plot3 = fig1.add_subplot(223)
plot3.scatter(x, y, color="purple")
plot3.plot(xx, y4, color="green")
plot4 = fig1.add_subplot(224)
plot4.scatter(x, y, color="purple")
plot4.plot(xx, y5, color="blue")

npx = np.array(x)
npy = np.array(y)
poly = interpolate.interp1d(npx, npy, 3)
poly_y = poly(x)

xnew = np.linspace(a, b, 601)
ynew = poly(xnew)

plot1.plot(xnew, ynew, color="gray")
plot2.plot(xnew, ynew, color="gray")
plot3.plot(xnew, ynew, color="gray")
plot4.plot(xnew, ynew, color="gray")

plot1.grid(linestyle='--')
plot1.set_xlabel("X")
plot1.set_ylabel("F(x)")
plot1.set_title("Полином 2-й степени")
plot2.grid(linestyle='--')
plot2.set_xlabel("X")
plot2.set_ylabel("F(x)")
plot2.set_title("Полином 3-й степени")
plot3.grid(linestyle='--')
plot3.set_xlabel("X")
plot3.set_ylabel("F(x)")
plot3.set_title("Полином 4-й степени")
plot4.grid(linestyle='--')
plot4.set_xlabel("X")
plot4.set_ylabel("F(x)")
plot4.set_title("Полином 5-й степени")
canvas = FigureCanvasTkAgg(fig1, master = win)
canvas.draw()
canvas.get_tk_widget().place(x=-50, y=-40)

img = PhotoImage(file = 'func.png')
photo = Label(win, image=img)
photo.place(x=150, y=10)

#Табулирование
xx = a
yy = 40
k = 810
lbl("x", k, 10)
lbl("f(x)", k+45, 10)
for i in range(n+1):
    lbl(f"%0.1f"%xx, k-10, yy)
    lbl(f"%0.3f"%f(xx), k+35, yy)
    yy += 30
    xx += dx

k += 140
xx = a
yy = 40
lbl("2-й степ.", k-10, 10)
for i in range(n+1):
    lbl(f"%0.3f"%y2[i*5], k, yy)
    yy += 30
    xx += dx
k += 85
lbl("абс. погр.", k-10, 10)
xx = a
yy = 40
for i in range(n+1):
	lbl(f"%0.3f"%(abs(y[i]-y2[i*5])), k, yy)
	yy += 30
	xx += dx
k += 80
lbl("отн. погр.", k+5, 10)
xx = a
yy = 40
for i in range(n+1):
	if y[i] != 0:
		lbl(f"%0.3f"%(100*(abs(y[i]-y2[i*5]))/y[i])+" %", k+10, yy)
	yy += 30
	xx += dx

k += 110
xx = a
yy = 40
lbl("3-й степ.", k-10, 10)
for i in range(n+1):
    lbl(f"%0.3f"%y3[i*5], k, yy)
    yy += 30
    xx += dx
k += 85
lbl("абс. погр.", k-10, 10)
xx = a
yy = 40
for i in range(n+1):
	lbl(f"%0.3f"%(abs(y[i]-y3[i*5])), k, yy)
	yy += 30
	xx += dx
k += 80
lbl("отн. погр.", k+5, 10)
xx = a
yy = 40
for i in range(n+1):
	if y[i] != 0:
		lbl(f"%0.3f"%(100*(abs(y[i]-y3[i*5]))/y[i])+" %", k+10, yy)
	yy += 30
	xx += dx

k += 120
xx = a
yy = 40
lbl("scipy", k-10, 10)
for i in range(n+1):
    lbl(f"%0.3f"%ynew[i*75], k, yy)
    yy += 30
    xx += dx
k += 85
lbl("абс. погр.", k-10, 10)
xx = a
yy = 40
for i in range(n+1):
	lbl(f"%0.3f"%(abs(y[i]-ynew[i*75])), k, yy)
	yy += 30
	xx += dx
k += 80
lbl("отн. погр.", k+5, 10)
xx = a
yy = 40
for i in range(n+1):
	if y[i] != 0:
		lbl(f"%0.3f"%(100*(abs(y[i]-ynew[i*75]))/y[i])+" %", k+10, yy)
	yy += 30
	xx += dx

xx = a
yy = 350
k = 810
lbl("x", k, yy)
lbl("f(x)", k+45, yy)
for i in range(n+1):
    lbl(f"%0.1f"%xx, k-10, yy+30)
    lbl(f"%0.3f"%f(xx), k+35, yy+30)
    yy += 30
    xx += dx

k += 140
xx = a
yy = 350
lbl("4-й степ.", k-10, yy)
for i in range(n+1):
    lbl(f"%0.3f"%y4[i*5], k, yy+30)
    yy += 30
    xx += dx
yy = 350
k += 85
lbl("абс. погр.", k-10, yy)
xx = a
yy = 350
for i in range(n+1):
	lbl(f"%0.3f"%(abs(y[i]-y4[i*5])), k, yy+30)
	yy += 30
	xx += dx
k += 80
yy = 350
lbl("отн. погр.", k+5, yy)
xx = a
yy = 350
for i in range(n+1):
	if y[i] != 0:
		lbl(f"%0.3f"%(100*(abs(y[i]-y4[i*5]))/y[i])+" %", k+10, yy+30)
	yy += 30
	xx += dx

k += 110
xx = a
yy = 350
lbl("5-й степ.", k-10, yy)
for i in range(n+1):
    lbl(f"%0.3f"%y5[i*5], k, yy+30)
    yy += 30
    xx += dx
k += 85
yy = 350
lbl("абс. погр.", k-10, yy)
xx = a
yy = 350
for i in range(n+1):
	lbl(f"%0.3f"%(abs(y[i]-y5[i*5])), k, yy+30)
	yy += 30
	xx += dx
k += 80
yy = 350
lbl("отн. погр.", k+5, yy)
xx = a
yy = 350
for i in range(n+1):
	if y[i] != 0:
		lbl(f"%0.3f"%(100*(abs(y[i]-y5[i*5]))/y[i])+" %", k+10, yy+30)
	yy += 30
	xx += dx

# Написание полиномов
k = 2
yy = 660
for i in [kefs_2, kefs_3, kefs_4, kefs_5]:
	s = ""
	s += f"Полином {k}-й степени: "
	for j in range(len(i)-1, -1, -1):
		if i[j] < 0:
			s += "(" + str(round(i[j], 3)) + ")"
		else:
			s += str(round(i[j], 3))
		if j != 0:
			s += f"*x^{j}"
			s += " + "
	lbl(s, 800, yy)
	k += 1
	yy += 30
win.mainloop()


#сцыпи