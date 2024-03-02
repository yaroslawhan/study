from sympy import *
from dichotomy import *
from chords import *
from tangent_Newton import *
from iteration import *
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Блок данных
ents = {}
lbls = []
lblsf = []
count_calc = 0
count_final_table = 0

# Функции в разных формах
x1 = symbols("x1")
y = x1**5 + x1 - 1

def f(x):
    return (x**5 + x - 1)

def f1(x):
    return (1 - x**5)

#Функция для вычисления корней
def calculation(method):
    if method == 1:
        tup = dichotomy(float(ents["a"].get()), float(ents["b"].get()), float(ents["eps"].get()), f)
        if tup == "Корней нет": x = tup
        else: x, xl, count = tup
    elif method == 2:
        tup = chords(float(ents["a"].get()), float(ents["b"].get()), float(ents["eps"].get()), x1, y, f)
        if tup == "Корней нет" or tup == "Ряд не сходится": x = tup
        else: x, xl, count = tup
    elif method == 3:
        tup = tangent(float(ents["a"].get()), float(ents["b"].get()), float(ents["eps"].get()), x1, y, f)
        if tup == "Корней нет": x = tup
        else: x, xl, count = tup
    else:
        tup = iteration(float(ents["a"].get()), float(ents["b"].get()), float(ents["eps"].get()), x1, y, f)
        if tup == "Корней нет" or tup == "Ряд не сходится": x = tup
        else: x, xl, count = tup
    if tup == "Корней нет" or tup == "Ряд не сходится":
        return tup, x
    else:
        return tup, x, xl, count


#Функции для окна
def lbl(t, xx, yy):
    l = Label(win, text=t, font=("Arial", 14))
    l.place(x=xx, y=yy)
def ent(key, xx, yy):
    ents[key] = Entry(win)
    ents[key].place(x=xx, y=yy)
def btn(command, text, xx, yy):
    btt = Button(command=command, text=text, font=("Arial", 14))
    btt.place(x=xx, y=yy, width = 200, height = 30)
def root_output(method, xx, yy):
    global count_calc
    count_calc += 1
    tup = calculation(method)
    xx += 220
    if count_calc > 1:
        for i in range(len(lbls)):
            lbls[i].destroy()
        lbls.clear()
    if tup[0] == "Корней нет" or tup[0] == "Ряд не сходится":
        lbls.append(Label(win, text=tup[1], font=("Arial", 14)))
        lbls[0].place(x=xx, y=yy)
    else:
        lbls.append(Label(win, text="x:", font=("Arial", 14)))
        lbls[0].place(x=xx, y=yy)
        #lbl("x:", xx, yy)
        xx += 30
        for i in range(tup[3]):
            lbls.append(Label(win, text=f"%0.3f"%tup[2][i], font=("Arial", 14)))
            lbls[i+1].place(x=xx, y=yy)
            #lbl(f"%0.3f"%xl[i], xx, yy)
            xx += 60
def final_table():
    lbl("Метод вычисления", 950, 10)
    lbl("Значение корня", 1200, 10)
    lbl("Кол-во итераций", 1400, 10)
    lbl("Дихотомия", 950, 50)
    lbl("Хорды", 950, 90)
    lbl("Касательные", 950, 130)
    lbl("Итерации", 950, 170)
    lbl("Библ. функции", 950, 210)
    global count_final_table
    count_final_table += 1
    xx = 1250
    yy = 50
    if count_final_table > 1:
        for i in range(len(lblsf)):
            lblsf[i].destroy()
        lblsf.clear()
    for i in range(1, 5):
        xx = 1250
        tup = calculation(i)
        if tup[0] == "Корней нет" or tup[0] == "Ряд не сходится":
            lblsf.append(Label(win, text=tup[1], font=("Arial", 14)))
            lblsf[-1].place(x=xx, y=yy)
        else:
            lblsf.append(Label(win, text=f"%0.3f"%tup[1], font=("Arial", 14)))
            lblsf[-1].place(x=xx, y=yy)
            xx += 200
            lblsf.append(Label(win, text=tup[3], font=("Arial", 14)))
            lblsf[-1].place(x=xx, y=yy)
        yy += 40
    #lbl(f"%0.3f"%(dichotomy(float(ents["a"].get()), float(ents["b"].get()), float(ents["eps"].get()), f)[2]), 1300, 50)

#Создание окна
win = Tk()
win.title("Лаб. 1, Ханевский Я., вар. 26")
win.geometry("1700x800")

#Табулирование
xx = -1
yy = 40
lbl("x", 25, 10)
lbl("f(x)", 70, 10)
for i in range(21):
    lbl(f"%0.1f"%xx, 10, yy)
    lbl(f"%0.3f"%f(xx), 60, yy)
    yy += 30
    xx += 0.1

#Построение графика
x = [i/10 for i in range(-10, 11)]
yy = [f(x[i]) for i in range(len(x))]
fig = Figure(figsize = (5, 5))
plot1 = fig.add_subplot(111)
plot1.plot(x, yy, color="purple")
x = tangent(-1, 1, 0.001, x1, y, f)[0]
plot1.plot(x, f(x),'ro')
plot1.grid(linestyle='--')
plot1.set_xlabel("x", fontsize=14)
plot1.set_ylabel("F(x)")
plot1.set_title("F(x) = x^5 + x - 1")
canvas = FigureCanvasTkAgg(fig, master = win)
canvas.draw()
canvas.get_tk_widget().place(x=140, y=10)

#Ввод данных
lbl("Введите левую границу:", 650, 10)
ent("a", 650, 50)
ents["a"].focus()
lbl("Введите правую границу:", 650, 100)
ent("b", 650, 140)
lbl("Введите значение точности:", 650, 190)
ent("eps", 650, 230)

#Вычисление корня
xx = 140
yy = 530
btn(lambda: root_output(1, xx, yy), "Метод дихотомии", xx, yy)
btn(lambda: root_output(2, xx, yy+30), "Метод хорд", xx, yy+30)
btn(lambda: root_output(3, xx, yy+60), "Метод касательных", xx, yy+60)
btn(lambda: root_output(4, xx, yy+90), "Метод итераций", xx, yy+90)

# Итоговая таблица
btn(final_table, "Итоговая таблица", 650, 300)

win.mainloop()