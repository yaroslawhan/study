from tkinter import *
from math import *
win = Tk()
win.config(cursor="coffee_mug")
win.title("Ханевский Ярослав, АС-23-04, вар. №27")
win.geometry("1000x800")
win.config(bg="darkblue") 

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
b = [[1.2, 8, 4, 1],
     [7.5, 3, 1.2, 6],
     [-2, 1, -1, -7],
     [5, 4, 3, 2]]
lbl = Label(win, text='Матрица A: ', cursor='spraycan').place(x=150, y=270)
x1 = 150
y1 = 310
for i in range(len(a)):
    x1 = 150
    for j in range(len(a[0])):
        lbl = Label(win, text=a[i][j], cursor='spraycan')
        lbl.place(x=x1, y=y1)
        x1 += 20
    y1 += 30    
lbl = Label(win, text='Матрица B: ', cursor='spraycan').place(x=150, y=y1+30)
x1 = 150
y1 = y1+70
for i in range(len(b)):
    x1 = 150
    for j in range(len(b[0])):
        lbl = Label(win, text=b[i][j], cursor='spraycan')
        lbl.place(x=x1, y=y1)
        x1 += 30
    y1 += 30

def trace(s):
    tr = 0
    for i in range(len(s)):
        tr += s[i][i]
    return tr
             
    
img = PhotoImage(file = '2.png')
photo = Label(win, image=img).place(x=150, y=0)
lbl = Label(win, text="x", cursor='spraycan')
lbl.place(x=500, y=270)
lbl = Label(win, text="y", cursor='spraycan')
lbl.place(x=550, y=270)
x1 = 500
y1 = 300
for i in range(0, 11):
    x1 = 500
    if i == 0: x = 0
    else: x = i/10
    c = trace(a)
    d = trace(b)
    y = c * x**2 + d
    lbl = Label(win, text=x, cursor='spraycan')
    lbl.place(x=x1, y=y1)
    x1 += 50
    lbl = Label(win, text="%.3f"%y, cursor='spraycan')
    lbl.place(x=x1, y=y1) 
    y1 += 30
win.mainloop()