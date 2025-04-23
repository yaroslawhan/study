from math import *
from matplotlib.pyplot import *
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Блок данных
h = 0.1
x = [i/10 for i in range(0, 11)]
y_eul = [[3, -3]]
def yx(x):
	return ((x+2)*e**(2*x) + e**(3*x)), (-2*(1+x)*e**(2*x) - e**(3*x))

def y1(x, y):
	return (4*y[0] + y[1] - e**(2*x)), (-2*y[0] + y[1])

y1num_eul = [[y1(x[0], y_eul[0])[i] for i in range(len(y_eul[0]))]]
dy_eul = [[h*y1num_eul[0][i] for i in range(len(y1num_eul[0]))]]
y_accur = [[yx(x[i])[j] for j in range(len(yx(x[0])))] for i in range(len(x))]

# Метод Эйлера
for i in range(1, int((x[-1]-x[0])//h)+2):
	y_eul.append([y_eul[i-1][j]+dy_eul[i-1][j] for j in range(len(y_eul[0]))])
	y1num_eul.append([y1(x[i], y_eul[i])[j] for j in range(len(y_eul[0]))])
	dy_eul.append([h*y1num_eul[i][j] for j in range(len(y1num_eul[0]))])

# for i in range(len(y_eul)):
# 	print(y_eul[i], y_accur[i])
# print("\n")


# Блок данных
y_runge = [[3, -3]]
y1num_runge = []
dy_runge = []

# Метод Рунге-Кутта
for i in range(0, int((x[-1]-x[0])//h)+1):
	y1num_runge.append([y1(x[i], y_runge[i])[j] for j in range(len(y_runge[0]))])
	k1 = [h*y1(x[i], y_runge[i])[j] for j in range(len(y_runge[0]))]
	k2 = [h*y1(x[i]+h/2, [y_runge[i][k]+k1[k]/2 for k in range(len(y_runge[0]))])[j] for j in range(len(y_runge[0]))]
	k3 = [h*y1(x[i]+h/2, [y_runge[i][k]+k2[k]/2 for k in range(len(y_runge[0]))])[j] for j in range(len(y_runge[0]))]
	k4 = [h*y1(x[i]+h, [y_runge[i][k]+k3[k] for k in range(len(y_runge[0]))])[j] for j in range(len(y_runge[0]))]
	dy_runge.append([(k1[j]+2*k2[j]+2*k3[j]+k4[j])/6 for j in range(len(y_runge[0]))])
	y_runge.append([y_runge[i][j]+dy_runge[i][j] for j in range(len(y_runge[0]))])

# for i in range(len(y_runge)):
# 	print(y_runge[i], y_accur[i])


# Отрисовка
#Функция для окна
def lbl(t, xx, yy):
    l = Label(win, text=t, font=("Arial", 13), bg="white")
    l.place(x=xx, y=yy)

# Отрисовка окна
win = Tk()
win.geometry("1900x820")
win.configure(background="white")
win.title("Ханевский, АС-23-04, вар.26")

fig1 = Figure(figsize = (10, 10))
plot1 = fig1.add_subplot(221)
for k in range(len(y_accur[0])):
	plot1.plot([x[i] for i in range(len(x))], [y_accur[i][k] for i in range(len(y_accur))], color="purple", linewidth=2)
	plot1.plot([x[i] for i in range(len(x))], [y_eul[i][k] for i in range(len(y_eul))], color="red", linewidth=2)
plot1.grid(linestyle='--')
plot1.set_xlabel("X")
plot1.set_ylabel("Y")
plot1.set_title("Метод Эйлера")

plot2 = fig1.add_subplot(222)
for k in range(len(y_accur[0])):
	plot2.plot([x[i] for i in range(len(x))], [y_accur[i][k] for i in range(len(y_accur))], color="purple", linewidth=2)
	plot2.plot([x[i] for i in range(len(x))], [y_runge[i][k] for i in range(len(y_runge))], color="red", linewidth=2)
plot2.grid(linestyle='--')
plot2.set_xlabel("X")
plot2.set_ylabel("Y")
plot2.set_title("Метод Рунге-Кутта")

canvas = FigureCanvasTkAgg(fig1, master = win)
canvas.draw()
canvas.get_tk_widget().place(x=-50, y=-80)

# Табулирование
yy = 70
k = 890
lbl("Метод Эйлера", k+180, 10)
lbl("x", k, 40)
lbl("y1(x)", k+45, 40)
for i in range(len(x)):
    lbl(f"%0.1f"%x[i], k-10, yy)
    lbl(f"%0.3f"%y_eul[i][0], k+35, yy)
    yy += 30
k += 70
yy = 70
lbl("y2(x)", k+45, 40)
for i in range(len(x)):
    lbl(f"%0.3f"%y_eul[i][1], k+35, yy)
    yy += 30
k += 105
yy = 70
lbl("y'1(x)", k+7, 40)
for i in range(len(y1num_eul)):
    lbl(f"%0.3f"%y1num_eul[i][0], k, yy)
    yy += 30
k += 75
yy = 70
lbl("y'2(x)", k+7, 40)
for i in range(len(y1num_eul)):
    lbl(f"%0.3f"%y1num_eul[i][1], k, yy)
    yy += 30
k += 75
yy = 70
lbl("dy1", k+10, 40)
for i in range(len(dy_eul)):
    lbl(f"%0.3f"%dy_eul[i][0], k, yy)
    yy += 30
k += 70
yy = 70
lbl("dy2", k+10, 40)
for i in range(len(dy_eul)):
    lbl(f"%0.3f"%dy_eul[i][1], k, yy)
    yy += 30
k += 70
yy = 70
lbl("y1(x) точн.", k-10, 40)
for i in range(len(y_accur)):
    lbl(f"%0.3f"%y_accur[i][0], k, yy)
    yy += 30
k += 90
yy = 70
lbl("y2(x) точн.", k-10, 40)
for i in range(len(y_accur)):
    lbl(f"%0.3f"%y_accur[i][1], k, yy)
    yy += 30
k += 90
lbl("абс. погр.1", k-10, 40)
yy = 70
for i in range(len(y_accur)):
	lbl(f"%0.3f"%(abs(y_accur[i][0]-y_eul[i][0])), k, yy)
	yy += 30
k += 90
lbl("абс. погр.2", k-10, 40)
yy = 70
for i in range(len(y_accur)):
	lbl(f"%0.3f"%(abs(y_accur[i][1]-y_eul[i][1])), k, yy)
	yy += 30
k += 80
lbl("отн. погр.1", k+5, 40)
yy = 70
for i in range(len(y_accur)):
	if y_accur[i] != 0:
		lbl(f"%0.3f"%(100*(abs(abs(y_accur[i][0]-y_eul[i][0])/y_accur[i][0])))+" %", k+10, yy)
	yy += 30
k += 90
lbl("отн. погр.2", k+5, 40)
yy = 70
for i in range(len(y_accur)):
	if y_accur[i] != 0:
		lbl(f"%0.3f"%(100*(abs(abs(y_accur[i][1]-y_eul[i][1])/y_accur[i][1])))+" %", k+10, yy)
	yy += 30

yy = 70+400
k = 890
lbl("Метод Рунге-Кутта", k+180, 10+400)
lbl("x", k, 40+400)
lbl("y1(x)", k+45, 40+400)
for i in range(len(x)):
    lbl(f"%0.1f"%x[i], k-10, yy)
    lbl(f"%0.3f"%y_runge[i][0], k+35, yy)
    yy += 30
k += 70
yy = 70+400
lbl("y2(x)", k+45, 40+400)
for i in range(len(x)):
    lbl(f"%0.3f"%y_runge[i][1], k+35, yy)
    yy += 30
k += 105
yy = 70+400
lbl("y'1(x)", k+7, 40+400)
for i in range(len(y1num_runge)):
    lbl(f"%0.3f"%y1num_runge[i][0], k, yy)
    yy += 30
k += 75
yy = 70+400
lbl("y'2(x)", k+7, 40+400)
for i in range(len(y1num_runge)):
    lbl(f"%0.3f"%y1num_runge[i][1], k, yy)
    yy += 30
k += 75
yy = 70+400
lbl("dy1", k+10, 40+400)
for i in range(len(dy_runge)):
    lbl(f"%0.3f"%dy_runge[i][0], k, yy)
    yy += 30
k += 70
yy = 70+400
lbl("dy2", k+10, 40+400)
for i in range(len(dy_runge)):
    lbl(f"%0.3f"%dy_runge[i][1], k, yy)
    yy += 30
k += 70
yy = 70+400
lbl("y1(x) точн.", k-10, 40+400)
for i in range(len(y_accur)):
    lbl(f"%0.3f"%y_accur[i][0], k, yy)
    yy += 30
k += 90
yy = 70+400
lbl("y2(x) точн.", k-10, 40+400)
for i in range(len(y_accur)):
    lbl(f"%0.3f"%y_accur[i][1], k, yy)
    yy += 30
k += 90
lbl("абс. погр.1", k-10, 40+400)
yy = 70+400
for i in range(len(y_accur)):
	lbl(f"%0.3f"%(abs(y_accur[i][0]-y_runge[i][0])), k, yy)
	yy += 30
k += 90
lbl("абс. погр.2", k-10, 40+400)
yy = 70+400
for i in range(len(y_accur)):
	lbl(f"%0.3f"%(abs(y_accur[i][1]-y_runge[i][1])), k, yy)
	yy += 30
k += 80
lbl("отн. погр.1", k+5, 40+400)
yy = 70+400
for i in range(len(y_accur)):
	if y_accur[i] != 0:
		lbl(f"%0.3f"%(100*(abs(abs(y_accur[i][0]-y_runge[i][0])/y_accur[i][0])))+" %", k+10, yy)
	yy += 30
k += 90
lbl("отн. погр.2", k+5, 40+400)
yy = 70+400
for i in range(len(y_accur)):
	if y_accur[i] != 0:
		lbl(f"%0.3f"%(100*(abs(abs(y_accur[i][1]-y_runge[i][1])/y_accur[i][1])))+" %", k+10, yy)
	yy += 30

img = PhotoImage(file = 'img_2.png')
photo = Label(win, image=img)
photo.place(x=80, y=450)

win.mainloop()