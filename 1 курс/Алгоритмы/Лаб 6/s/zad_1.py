from math import *
from matplotlib.pyplot import *
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Блок данных
h = 0.1
x = [i/10 for i in range(0, 11)]
y_eul = [1]
def yx(x):
	return 2*e**(x**2) - x**2 - 1

def y1(x, y):
	return 2*x*(x**2 + y)

y1num_eul = [y1(x[0], y_eul[0])]
dy_eul = [h*y1num_eul[0]]
y_accur = [yx(x[i]) for i in range(len(x))]

# Метод Эйлера
for i in range(1, int((x[-1]-x[0])//h)+2):
	y_eul.append(y_eul[i-1]+dy_eul[i-1])
	y1num_eul.append(y1(x[i], y_eul[i]))
	dy_eul.append(h*y1num_eul[i])

print(x)
print(y_eul)
print(y_accur)
print(y1num_eul)
print(dy_eul)

# Блок данных
y_runge = [1]
y1num_runge = []
dy_runge = []

# Метод Рунге-Кутта
for i in range(0, int((x[-1]-x[0])//h)+1):
	y1num_runge.append(y1(x[i], y_runge[i]))
	k1 = h*y1(x[i], y_runge[i])
	k2 = h*y1(x[i]+h/2, y_runge[i]+k1/2)
	k3 = h*y1(x[i]+h/2, y_runge[i]+k2/2)
	k4 = h*y1(x[i]+h, y_runge[i]+k3)
	dy_runge.append((k1+2*k2+2*k3+k4)/6)
	y_runge.append(y_runge[i]+dy_runge[i])

# print(y_runge)
# print(dy_runge)


# Отрисовка
#Функция для окна
def lbl(t, xx, yy):
    l = Label(win, text=t, font=("Arial", 14), bg="white")
    l.place(x=xx, y=yy)

# Отрисовка окна
win = Tk()
win.geometry("1500x820")
win.configure(background="white")
win.title("Ханевский, АС-23-04, вар.26")

fig1 = Figure(figsize = (10, 10))
plot1 = fig1.add_subplot(221)
plot1.plot(x, y_accur, color="purple")
plot1.plot(x, y_eul, color="red")
plot1.grid(linestyle='--')
plot1.set_xlabel("X")
plot1.set_ylabel("Y")
plot1.set_title("Метод Эйлера")

plot2 = fig1.add_subplot(222)
plot2.plot(x, y_accur, color="purple")
plot2.plot(x, y_runge, color="red")
plot2.grid(linestyle='--')
plot2.set_xlabel("X")
plot2.set_ylabel("Y")
plot2.set_title("Метод Рунге-Кутта")

canvas = FigureCanvasTkAgg(fig1, master = win)
canvas.draw()
canvas.get_tk_widget().place(x=-40, y=-80)

# Табулирование
yy = 70
k = 900
lbl("Метод Эйлера", k+180, 10)
lbl("x", k, 40)
lbl("y(x)", k+45, 40)
for i in range(len(x)):
    lbl(f"%0.1f"%x[i], k-10, yy)
    lbl(f"%0.3f"%y_eul[i], k+35, yy)
    yy += 30
k += 105
yy = 70
lbl("y'(x)", k+7, 40)
for i in range(len(y1num_eul)):
    lbl(f"%0.3f"%y1num_eul[i], k, yy)
    yy += 30
k += 70
yy = 70
lbl("dy", k+10, 40)
for i in range(len(dy_eul)):
    lbl(f"%0.3f"%dy_eul[i], k, yy)
    yy += 30
k += 70
yy = 70
lbl("y(x) точн.", k-10, 40)
for i in range(len(y_accur)):
    lbl(f"%0.3f"%y_accur[i], k, yy)
    yy += 30
k += 90
lbl("абс. погр.", k-10, 40)
yy = 70
for i in range(len(y_accur)):
	lbl(f"%0.3f"%(abs(y_accur[i]-y_eul[i])), k, yy)
	yy += 30
k += 80
lbl("отн. погр.", k+5, 40)
yy = 70
for i in range(len(y_accur)):
	if y_accur[i] != 0:
		lbl(f"%0.3f"%(100*(abs(y_accur[i]-y_eul[i]))/y_accur[i])+" %", k+10, yy)
	yy += 30

yy = 70+400
k = 900
lbl("Метод Рунге-Кутта", k+170, 10+400)
lbl("x", k, 40+400)
lbl("y(x)", k+45, 40+400)
for i in range(len(x)):
    lbl(f"%0.1f"%x[i], k-10, yy)
    lbl(f"%0.3f"%y_runge[i], k+35, yy)
    yy += 30
k += 105
yy = 70+400
lbl("y'(x)", k+7, 40+400)
for i in range(len(y1num_runge)):
    lbl(f"%0.3f"%y1num_runge[i], k, yy)
    yy += 30
k += 70
yy = 70+400
lbl("dy", k+10, 40+400)
for i in range(len(dy_runge)):
    lbl(f"%0.3f"%dy_runge[i], k, yy)
    yy += 30
k += 70
yy = 70+400
lbl("y(x) точн.", k-10, 40+400)
for i in range(len(y_accur)):
    lbl(f"%0.3f"%y_accur[i], k, yy)
    yy += 30
k += 90
lbl("абс. погр.", k-10, 40+400)
yy = 70+400
for i in range(len(y_accur)):
	lbl(f"%0.3f"%(abs(y_accur[i]-y_runge[i])), k, yy)
	yy += 30
k += 80
lbl("отн. погр.", k+5, 40+400)
yy = 70+400
for i in range(len(y_accur)):
	if y_accur[i] != 0:
		lbl(f"%0.3f"%(100*(abs(y_accur[i]-y_runge[i]))/y_accur[i])+" %", k+10, yy)
	yy += 30

img = PhotoImage(file = 'img_1.png')
photo = Label(win, image=img)
photo.place(x=80, y=450)

win.mainloop()