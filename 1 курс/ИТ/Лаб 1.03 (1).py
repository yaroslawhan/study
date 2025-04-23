import tkinter as tk
import math
from tkinter import messagebox
#tk.messagebox. YESNOCANCEL.isalnum
win = tk.Tk()
win.config(cursor="fleur")
win.title("Ханевский Ярослав")
win.geometry("400x250")
win.config(bg="darkblue") #yellowgreen, lightblue, pink, darkblue, darkred, lightgray
#tk.messagebox.showerror('', 'нет решений')
x = [29.3, 0, -1.1, 0.94, 0, 9.3, -1.2, 0, -7.93, 0]
def gety():
#     y = ""
    y = []
    y1 = ""
    for i in range(len(x)):
        for j in range(len(x)):
            if i != j and x[j]!=0:
                y.append(x[i]/x[j])
                if "%.3f"%(x[i]/x[j]) == "-0.000":
                    y1 += ", " + "%.3f"%0
                else: y1 += ", " + "%.3f"%(x[i]/x[j])
    y1 = y1[2:]
    vivody.insert(0, y1) # Вывод в нулевуо строкy y1
# vivodx.insert(0, x)
zadanie_image = tk.PhotoImage(file='задание_для_3.png')
tk.Label(win, image=zadanie_image, cursor="man").pack()
lbl1=tk.Label(win, text = f"X = {x}", cursor="coffee_mug")
lbl1.place(x=90,y=91)
lbl2=tk.Label(win, text = "Y = ", cursor="spraycan")
lbl2.place(x=90,y=191)
btn1= tk.Button(win, text="считаем Y", command=gety, relief=tk. RAISED, cursor="star")
btn1.config(background='LightCoral')
btn1.place(x=90,y=150)
# vivodx=tk.Entry(win, foreground='MediumSeaGreen', font='bold')
# vivodx.place(x=100,y=91)
vivody=tk.Entry(win, foreground='MediumSeaGreen', font='bold', cursor="trek")
vivody.place(x=130,y=190)
win.mainloop()
#'%.4f' % y[n]
#-0.0009 <= x[i]/x[j] <= 0: