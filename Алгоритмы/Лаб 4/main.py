from left_rect import left_rect
from mid_rect import mid_rect
from right_rect import right_rect
from trap import trap
from simpson import simpson
from math import *
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.integrate import quad, simps

#Блок данных
eps = 10**(-10)
ents = {}
lbls = []
analit_int = (2/3)*((log(5)**(3/2))-1)
table_int = pi*log(4)
x = [0, 0.26, 0.52, 0.79, 1.05, 1.31, 1.57, 1.83, 2.09, 2.36, 2.62, 2.88, 3.14]
y = [0, 0.13, 0.43, 0.78, 1.1, 1.38, 1.61, 1.8, 1.95, 2.06, 2.14, 2.18, 2.2]

#Подынтегральная функция
def f(x):
	return ((log(x))/(x*(log(x))**(1/2)))

#Функции для кнопок
def but(method, y1):
	mode = ents["mode"].get()
	if len(lbls) != 0: lbls[0].destroy()
	lbls.clear()
	if mode == "1" or mode == "2":
		if mode == "1":
			if method == 1:
				result = left_rect(f, 1, int(ents["n"].get()), e, 5, float(ents["eps"].get()))
			if method == 2:
				result = mid_rect(f, 1, int(ents["n"].get()), e, 5, float(ents["eps"].get()))
			if method == 3:
				result = right_rect(f, 1, int(ents["n"].get()), e, 5, float(ents["eps"].get()))
			if method == 4:
				result = trap(f, 1, int(ents["n"].get()), e, 5, float(ents["eps"].get()))
			if method == 5:
				result = simpson(f, 1, int(ents["n"].get()), e, 5, float(ents["eps"].get()))
			if method == 6:
				result = quad(f, e, 5)[0]
			integral = analit_int
		if mode == "2":
			if method == 1:
				result = left_rect(f, 2, x, y, float(ents["eps"].get()), None)
			if method == 2:
				result = mid_rect(f, 2, x, y, float(ents["eps"].get()), None)
			if method == 3:
				result = right_rect(f, 2, x, y, float(ents["eps"].get()), None)
			if method == 4:
				result = trap(f, 2, x, y, float(ents["eps"].get()), None)
			if method == 5:
				result = simpson(f, 2, x, y, float(ents["eps"].get()), None)
			if method == 6:
				result = simps(y, x)
			integral = table_int
		eps = float(ents["eps"].get())

		if str(eps).count("e")==0: result_round = round(result, len(str(eps).split('.')[1]))
		else: result_round = round(result, int(str(eps).split('e-')[1]))
		abs_pogr = abs(result - integral)
		otn_pogr = (abs_pogr/integral)*100
		if str(eps).count("e")==0: abs_pogr = round(abs_pogr, len(str(eps).split('.')[1]))
		else: abs_pogr = round(abs_pogr, int(str(eps).split('e-')[1]))
		if str(eps).count("e")==0: otn_pogr = round(otn_pogr, len(str(eps).split('.')[1]))
		else: otn_pogr = round(otn_pogr, int(str(eps).split('e-')[1]))
		lbls.append(Label(win, text=f"Значение интеграла: {result_round}, абсолют. погрешность: {abs_pogr}, относит. погрешность: {otn_pogr}%", font=("Arial", 14), background="white"))
		lbls[0].place(x=700, y=y1)
	else:
		lbls.append(Label(win, text="Введены неверные значения", font=("Arial", 14), background="white"))
		lbls[0].place(x=700, y=y1)

#Функции для окна
def lbl(t, xx, yy):
    l = ttk.Label(win, text=t, font=("Arial", 14), background="white")
    l.place(x=xx, y=yy)
def ent(key, xx, yy):
    ents[key] = ttk.Entry(win)
    ents[key].place(x=xx, y=yy)
def btn(command, text, xx, yy):
    btt = ttk.Button(command=command, text=text, style='Custom.TButton')
    btt.place(x=xx, y=yy, width = 220, height = 30)

#Создание окна
win = Tk()
win.title("Лаб. 4, Ханевский Я., вар. 26")
win.geometry("1620x1000")
win.config(cursor="diamond_cross")
win.config(bg="white")

#Построение графиков
xx = [i/10 for i in range(11, 101)]
yy = [f(xx[i]) for i in range(len(xx))]
fig1 = Figure(figsize = (5, 5))
plot1 = fig1.add_subplot(111)
plot1.plot(xx, yy, color="purple")
plot1.plot([e, e], [0, f(e)],'k--')
plot1.plot([5, 5], [0, f(5)],'k--')
plot1.set_xlim(1, 10)
plot1.set_ylim(0.1, 0.43)
plot1.grid(linestyle='--')
plot1.set_xlabel("x", fontsize=14)
plot1.set_ylabel("F(x)")
plot1.set_title("F(x) = log(x)/(x*(log(x))**(1/2))")
canvas = FigureCanvasTkAgg(fig1, master = win)
canvas.draw()
canvas.get_tk_widget().place(x=10, y=0)

fig2 = Figure(figsize = (5, 5))
plot2 = fig2.add_subplot(111)
plot2.plot(x, y, color="purple")
plot2.set_xlim(x[0], x[-1])
plot2.set_ylim(y[0], y[-1])
plot2.grid(linestyle='--')
plot2.set_xlabel("x", fontsize=14)
plot2.set_ylabel("F(x)")
plot2.set_title("Таблично заданная функция")
canvas = FigureCanvasTkAgg(fig2, master = win)
canvas.draw()
canvas.get_tk_widget().place(x=10, y=490)

##Вывод на форму таблицы и интеграла
img = PhotoImage(file = 'table.png')
photo = Label(win, image=img)
photo.place(x=470, y=879)
img1 = PhotoImage(file = 'integral.png')
photo1 = Label(win, image=img1)
photo1.place(x=470, y=58)

#Вывод точных численных значений интегралов 
lbl("Численное значение интеграла: 0.6945", 470, 138)
lbl("Численное значение интеграла: 4.3551", 470, 845)

#Создание полей для ввода данных
lbl("Введите число делений(n):", 470, 178)
ent("n", 470, 208)
lbl("Введите точность вычислений:", 470, 238)
ent("eps", 470, 268)
lbl("Выберите интеграл(аналитический - 1, табличный - 2):", 470, 298)
ent("mode", 470, 328)

# Создание стиля для кнопок
style = ttk.Style()
style.configure('Custom.TButton', font=('Arial', 14))

#Создание кнопок
btn(lambda: but(1, 368), "Метод левых прямоуг.", 470, 368)
btn(lambda: but(2, 403), "Метод средних прямоуг.", 470, 403)
btn(lambda: but(3, 438), "Метод правых прямоуг.", 470, 438)
btn(lambda: but(4, 473), "Метод трапеций", 470, 473)
btn(lambda: but(5, 508), "Метод Симпсона", 470, 508)
btn(lambda: but(6, 543), "Библиотечная функция", 470, 543)

win.mainloop()
# print(simpson(f, 2, x, y, eps, None))
# print(mid_rect(f, 2, x, y, eps, None))