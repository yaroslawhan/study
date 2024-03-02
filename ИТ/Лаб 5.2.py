from tkinter import *
from math import *
from random import randint
win = Tk()
win.config(cursor="coffee_mug")
win.title("Ханевский Ярослав, АС-23-04, вар. №27")
win.geometry("1000x800")
win.config(bg="darkgreen") 

x = [15.5, 18.3, 14.4, 19.1, 17.7]
y = [21.8, 22.3, 25.1, 24.3]
z = [19.5, 20.08, 21.1, 18.1, 19.5]
    
def expected(s):
    summ = 0
    for i in range(1, len(s)+1):
        summ += s[i-1]
    m = (1/(len(s)))*summ
    return m

def dispersion(s):
    summ = 0
    for i in range(1, len(s)+1):
        summ += (s[i-1])**2
    d = (1/(len(s)))*summ - (expected(s))**2
    return d

def average(s):
    ss = (dispersion(s))**(1/2)
    return ss
print(average(x))
             
    
img = PhotoImage(file = '3.png')
photo = Label(win, image=img).place(x=150, y=0)
lbl = Label(win, text="X = ", cursor='spraycan')
lbl.place(x=50, y=500)
x1 = 100
for i in range(len(x)):
    lbl = Label(win, text=x[i], cursor='spraycan')
    lbl.place(x=x1, y=500)
    x1 += 50
lbl = Label(win, text="Y = ", cursor='spraycan')
lbl.place(x=50, y=550)
x1 = 100
for i in range(len(y)):
    lbl = Label(win, text=y[i], cursor='spraycan')
    lbl.place(x=x1, y=550)
    x1 += 50
lbl = Label(win, text="Z = ", cursor='spraycan')
lbl.place(x=50, y=600)
x1 = 100
for i in range(len(z)):
    lbl = Label(win, text=z[i], cursor='spraycan')
    lbl.place(x=x1, y=600)
    x1 += 50

lbl = Label(win, text="X", cursor='spraycan')
lbl.place(x=500, y=500)
lbl = Label(win, text="Y", cursor='spraycan')
lbl.place(x=500, y=550)
lbl = Label(win, text="Z", cursor='spraycan')
lbl.place(x=500, y=600)

lbl = Label(win, text="Мат. ожидание", cursor='spraycan')
lbl.place(x=550, y=450)
lbl = Label(win, text="Дисперсия", cursor='spraycan')
lbl.place(x=650, y=450)
lbl = Label(win, text="Ср. квадр. значение", cursor='spraycan')
lbl.place(x=730, y=450)

lbl = Label(win, text="%.3f"%expected(x), cursor='spraycan')
lbl.place(x=580, y=500)
lbl = Label(win, text="%.3f"%expected(y), cursor='spraycan')
lbl.place(x=580, y=550)
lbl = Label(win, text="%.3f"%expected(z), cursor='spraycan')
lbl.place(x=580, y=600)

lbl = Label(win, text="%.3f"%dispersion(x), cursor='spraycan')
lbl.place(x=670, y=500)
lbl = Label(win, text="%.3f"%dispersion(y), cursor='spraycan')
lbl.place(x=670, y=550)
lbl = Label(win, text="%.3f"%dispersion(z), cursor='spraycan')
lbl.place(x=670, y=600)

lbl = Label(win, text="%.3f"%average(x), cursor='spraycan')
lbl.place(x=770, y=500)
lbl = Label(win, text="%.3f"%average(y), cursor='spraycan')
lbl.place(x=770, y=550)
lbl = Label(win, text="%.3f"%average(z), cursor='spraycan')
lbl.place(x=770, y=600)
win.mainloop()