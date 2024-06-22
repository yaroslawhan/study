import matplotlib.pyplot as plt
import random
from tkinter import *
from tkinter import ttk
from matplotlib.pyplot import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Блок данных
xlim = [0, 10]
ylim = [0, 10]
# dots = [[1, 3], [4.5, 5], [7.5, 4], [9, 3], [6, 1], [5, 3], [7, 3]]
# Число точек
n = 20
dots = [[random.randint(xlim[0], xlim[1]), random.randint(ylim[0], ylim[1])] for i in range(n)]
xses = [dots[i][0] for i in range(len(dots))]
ys = [dots[i][1] for i in range(len(dots))]
lines = [] # вложенные списки: [индекс 1-й точки, индекс 2-й точки, ..., индекс i-й точки, flag, a, b, c]
isUsed = [False for i in range(len(dots))] # True - точка использована

# Функция нахождения коэфф. прямой, проход. ч-з 2 точки
def find_line_kefs(dot1, dot2):
	# if dot1[0] == dot2[0]:
	# 	return False, 0, 0
	# else:
	# 	k = (dot2[1]-dot1[1])/(dot2[0]-dot1[0])
	# 	return True, k, (dot1[1]-k*dot1[0])
	A = dot2[1] - dot1[1]
	B = dot1[0] - dot2[0]
	C = dot2[0] * dot1[1] - dot1[0] * dot2[1]
	return A, B, C

# Проверка исключений
if len(dots) in [0, 1]:
	print("Множество точек состоит из 1 или 0 точек")
if len(dots) == 2:
	print(1)

# Основной код
c = 0 # Индекс прямой
for i in range(len(dots)-1):
	for j in range(i, len(dots)-1):
		kef_a, kef_b, kef_c = find_line_kefs(dots[i], dots[j+1])
		lines.append([i, j+1, kef_a, kef_b, kef_c])
		for k in range(len(dots)):
			if (k not in lines[c][0:-3]) and (kef_a*dots[k][0] + kef_b*dots[k][1] + kef_c == 0):
				for h in range(len(lines[c])-3):
					if (k > lines[c][h] and k < lines[c][h+1]) or (h == len(lines[c])-4):
						lines[c].insert(h+1, k)
						break
					if (h == 0) and (k < lines[c][h]):
						lines[c].insert(h, k)
						break

		c += 1
lines_before_count = len(lines)

# Удаляем прямые с кратными и равными нулю коэфф.
rep_c = 0 # Счётчик повторов
j = 0
while j < len(lines):
	if lines[j][-3:] == [0, 0, 0]:
		lines.pop(j)
	else:
		j += 1
for i in range(len(lines)-1):
	j = i+1
	while j < len(lines):
		if lines[i][:-3] == lines[j][:-3]:
			rep_c += 1
			lines.pop(j)
		else:
			j += 1
print(rep_c)
print(lines)
lines_after_count = len(lines)

# Покрытие точек
cover_lines = [] # Прямые, использ. для покрытия точек
while True:
	ind = 0 # Индекс прямой с макс. покрытием
	max_unused_dots_count = 0 # Макс. число непокрытых точек
	for i in range(len(lines)):
		unused_dots_count = 0 # Число непокрытых точек
		for j in range(len(lines[i])-3):
			if isUsed[lines[i][j]] == False:
				unused_dots_count += 1
		if unused_dots_count > max_unused_dots_count:
			max_unused_dots_count = unused_dots_count
			ind = i
	for i in range(len(lines[ind])-3):
		isUsed[lines[ind][i]] = True
	cover_lines.append(lines[ind])
	lines.pop(ind)

	if not False in isUsed:
		break
print(cover_lines)


# Отрисовка
#Функция для окна
def lbl(t, xx, yy):
    l = Label(win, text=t, font=("Arial", 14), bg="white")
    l.place(x=xx, y=yy)

win = Tk()
win.geometry("1300x680")
win.configure(background="white")
win.title("РГР №1, Ханевский, АС-23-04, вар.26")
fig1 = Figure(figsize = (7, 7))
plot1 = fig1.add_subplot(111)
plot1.scatter(xses, ys)

for i in range(len(cover_lines)):
	if cover_lines[i][-3] == 0 and cover_lines[i][-2] == 0 and cover_lines[i][-1] == 0:
		continue
	if cover_lines[i][-2] != 0:
		xmin = xlim[0]
		xmax = xlim[1]
		ymin = (-1)*(cover_lines[i][-3]*xmin + cover_lines[i][-1])/cover_lines[i][-2]
		ymax = (-1)*(cover_lines[i][-3]*xmax + cover_lines[i][-1])/cover_lines[i][-2]
	else:
		xmin = (-1)*cover_lines[i][-1]/cover_lines[i][-3]
		xmax = xmin
		ymin = ylim[0]
		ymax = ylim[1]
	plot1.plot([xmin, xmax], [ymin, ymax], "r-")

canvas = FigureCanvasTkAgg(fig1, master = win)
canvas.draw()
canvas.get_tk_widget().place(x=-20, y=-20)

img = PhotoImage(file = 'img.png')
photo = Label(win, image=img)
photo.place(x=650, y=60)

lbl(f"Число прямых до удаления повторяющихся: {lines_before_count}", 650, 160)
lbl(f"Число прямых после удаления повторяющихся: {lines_after_count}", 650, 190)
lbl(f"Число покрывающих прямых: {len(cover_lines)}", 650, 220)
win.mainloop()