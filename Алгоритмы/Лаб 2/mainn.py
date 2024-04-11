from jacobi import jacobi
from gauss_zeidel import gauss_zeidel
from newton import newton
from tkinter import *
from tkinter import ttk

# Блок данных
ents = {}
lbls = []
eps = 0.001

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

#Функции для кнопок
def but_j():
	x, y, count = jacobi(system_expr, system_unexpr, float(ents["x"].get()), float(ents["y"].get()), float(ents["eps"].get()))
	if len(lbls) != 0: lbls[0].destroy()
	lbls.clear()
	if isinstance(x, str):
		temp = f"x = {x}, y = {y}, итераций: {str(count)}"
	else: 
		temp = "x = " + f"%.3f"%x + ", y = " + f"%.3f"%y + ", итераций: " + str(count)
	lbls.append(Label(win, text=temp, font=("Arial", 14), background="white"))
	lbls[0].place(x=1243, y=276)
def but_gz():
	x, y, count = gauss_zeidel(system_expr, system_unexpr, float(ents["x"].get()), float(ents["y"].get()), float(ents["eps"].get()))
	if len(lbls) != 0: lbls[0].destroy()
	lbls.clear()
	if isinstance(x, str):
		temp = f"x = {x}, y = {y}, итераций: {str(count)}"
	else: 
		temp = "x = " + f"%.3f"%x + ", y = " + f"%.3f"%y + ", итераций: " + str(count)
	lbls.append(Label(win, text=temp, font=("Arial", 14), background="white"))
	lbls[0].place(x=1243, y=311)

# Системы в разных формах
def system_expr(x, y):
	return [(9*y-2*7/(7+1))**(1/4), (((x**2)*(y**2)-3*x**3+2*7)/6)**(1/3)]
	#return [(9*y-2*7/(7+1))**(1/4), ((3*x**3-2*7)/(x**2-6*y))**(1/2)]
	#return [((3*x**3+6*y**3-2*7)/y**2)**(1/2), (x**4+2*7/(7+1))/9]
def system_unexpr(x, y):
	return [(x**2)*(y**2) - 3*x**3 - 6*y**3 + 2*7, x**4 - 9*y + 2*(7/(7+1))]

#Создание окна
win = Tk()
win.title("Лаб. 2, Ханевский Я., вар. 26")
win.geometry("1700x677")
win.config(cursor="diamond_cross")
win.config(bg="white") 

#Вывод на форму графика и системы
img = PhotoImage(file = 'graphic.png')
photo = Label(win, image=img)
photo.place(x=10, y=10)
img1 = PhotoImage(file = 'system1.png')
photo1 = Label(win, image=img1)
photo1.place(x=1013, y=10)

#Создание полей для ввода данных
lbl("Введите x:", 1013, 76)
ent("x", 1013, 106)

lbl("Введите y:", 1013, 136)
ent("y", 1013, 166)

lbl("Введите погрешность:", 1013, 196)
ent("eps", 1013, 226)

# Создание стиля для кнопок
style = ttk.Style()
style.configure('Custom.TButton', font=('Arial', 14))

#Создание кнопок
btn(but_j, "Метод Якоби", 1013, 276)
btn(but_gz, "Метод Гаусса-Зейделя", 1013, 311)
btn(lambda: newton(system_expr, system_unexpr, float(ents["x"].get()), float(ents["y"].get()), float(ents["eps"].get())), "Метод Ньютона", 1013, 346)

win.mainloop()