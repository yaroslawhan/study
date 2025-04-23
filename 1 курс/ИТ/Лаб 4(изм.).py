from tkinter import *
from math import *
win = Tk()
win.config(cursor="coffee_mug")
win.title("Ханевский Ярослав, АС-23-04, вар. №27")
win.geometry("1500x800")
win.config(bg="darkgreen") 

def fac(x):
    
    for i in range(1, x):
        x *= i
    return x
n = 5
m = 6
lbl = Label(win, text='Введите x: ', cursor='spraycan').place(x=15, y=200)
xi = Entry(win)
xi.place(x=15, y=220)
lbl = Label(win, text='Введите y: ', cursor='spraycan').place(x=15, y=250)
yi = Entry(win)
yi.place(x=15, y=270)
a = [[0]*m for i in range(n)]
mx = a[0][0]
mn = a[0][0]
imx = 1
jmx = 1
imn = 1
jmn = 1

def func():
    x = int(xi.get())
    y = int(yi.get())
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i+j > 3:
                a[i-1][j-1] = log(j*sqrt(e**(x-y)))+x**i
            else:
                a[i-1][j-1] = x+((x**i)/fac(i))
    
    lbl = Label(win, text='Исходная матрица: ', cursor='spraycan').place(x=150, y=200)
    x1 = 170
    y1 = 240
    for i in range(len(a)):
        x1 = 170 - (i+1)*3
        for j in range(len(a[0])):
            lbl = Label(win, text="%.3f" %(a[i][j]), cursor='spraycan')
            lbl.place(x=x1, y=y1)
            x1 += 80
        y1 += 30
        
#     for i in range(len(a)):
#         for j in range(len(a[0])):
#             print("%.3f" %(a[i][j]), end=" ")
#         print("")
    
    x1 = 790
    y1 = 200          
    for i in range(1, n+1):
        mx = a[i-1][0]
        mn = a[i-1][0]
        imx = 1
        jmx = 1
        imn = 1
        jmn = 1    
        for j in range(1, m+1):
            if a[i-1][j-1] > mx:
                mx = a[i-1][j-1]
                imx = i
                jmx = j
            
            if a[i-1][j-1] < mn:
                mn = a[i-1][j-1]
                imn = i
                jmn = j
        if a[i-1][0] == mn:
            imn = i
            jmn = 1
        
        lbl = Label(win, text=f'Максимальный элемент {i} строки: %.3f. Индекс: {imx}, {jmx}'%mx, cursor='spraycan')
        lbl.place(x=x1, y=y1)
        y1 += 30
        lbl = Label(win, text=f'Минимальный элемент {i} строки: %.3f. Индекс: {imn}, {jmn}'%mn, cursor='spraycan')
        lbl.place(x=x1, y=y1)  
        y1 += 30
#         print(f'Максимальный элемент {i} строки: %.3f. Индекс: {imx}, {jmx}'%mx)
#         print(f'Минимальный элемент {i} строки: %.3f. Индекс: {imn}, {jmn}'%mn)
        a[imx-1][jmx-1], a[imn-1][jmn-1] = a[imn-1][jmn-1], a[imx-1][jmx-1]
        
    lbl = Label(win, text='Преобразованная матрица: ', cursor='spraycan').place(x=150, y=y1+30)
    x1 = 170
    y1 = y1+70
    for i in range(len(a)):
        x1 = 170 - (i+1)*3
        for j in range(len(a[0])):
            lbl = Label(win, text="%.3f" %(a[i][j]), cursor='spraycan')
            lbl.place(x=x1, y=y1)
            x1 += 80
        y1 += 30    
    
img = PhotoImage(file = '1.png')
photo = Label(win, image=img).place(x=150, y=0)
btn = Button(win, text="Считать", command=func, cursor="star").place(x=15, y=300)
win.mainloop()