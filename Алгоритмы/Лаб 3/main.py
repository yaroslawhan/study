from gausses import gausses
from gausses_jordan import gausses_jordan
from tkinter import *

# Блок данных
a = [[4.5, -3.5, 7.4], [3.1, -0.6, -2.3], [0.8, 7.4, -0.5]]
b = [2.5, -1.5, 6.4]

#Функции для окна
def lbl(t, xx, yy):
    l = Label(win, text=t, font=("Arial", 14))
    l.place(x=xx, y=yy)
def btn(command, text, xx, yy):
    btt = Button(command=command, text=text, font=("Arial", 13))
    btt.place(x=xx, y=yy, width = 200, height = 30)
def gausses_tk(a, b):
	x = gausses(a, b)
	lbl(f"x1=%.3f"%x[0], 20, 230)
	lbl(f"x2=%.3f"%x[1], 20, 260)
	lbl(f"x3=%.3f"%x[2], 20, 290)
def gausses_jordan_tk(a, b):
	x = gausses_jordan(a, b)
	lbl(f"x1=%.3f"%x[0], 250, 230)
	lbl(f"x2=%.3f"%x[1], 250, 260)
	lbl(f"x3=%.3f"%x[2], 250, 290)

win = Tk()
win.title("Лабораторная работа №3 Ханевский Вар. 26")
win.geometry("1280x720")

img = PhotoImage(file = '1.png')
photo = Label(win, image=img).place(x=20, y=20)

lbl("4.5x1 - 3.5x2 + 7.4x3 = 2.5\n 3.1x1 - 0.6x2 - 2.3x3 = -1.5\n 0.8x1 + 7.4x2 - 0.5x3 = 6.4\n ", 20, 120)
btn(lambda : gausses_tk(a, b), "Метод Гаусса", 20, 200)
btn(lambda : gausses_jordan_tk(a, b), "Метод Гаусса-Джордана", 250, 200)

#Вывод в файл
f = open("file.txt", "w")
f.write("Метод Гаусса: \n")
x = gausses(a, b)
f.write(f"x1=%.3f\n"%x[0])
f.write(f"x2=%.3f\n"%x[1])
f.write(f"x3=%.3f\n\n"%x[2])
f.write("Метод Гаусса-Джордана: \n")
x = gausses_jordan(a, b)
f.write(f"x1=%.3f\n"%x[0])
f.write(f"x2=%.3f\n"%x[1])
f.write(f"x3=%.3f\n"%x[2])
f.close()


win.mainloop()