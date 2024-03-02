from tkinter import *
from math import *
from random import randint
win = Tk()
win.config(cursor="coffee_mug")
win.title("Ханевский Ярослав, АС-23-04, вар. №27")
win.geometry("1500x1000")
win.config(bg="darkgreen") 

lbl = Label(win, text="Enter x: ", cursor='spraycan')
lbl.place(x=20, y=140)      
x = Entry(win, cursor="coffee_mug")
x.place(x=70, y=140)
lbl = Label(win, text="Enter y: ", cursor='spraycan')
lbl.place(x=20, y=180)      
y = Entry(win, cursor="coffee_mug")
y.place(x=70, y=180)
lbl = Label(win, text="Enter z: ", cursor='spraycan')
lbl.place(x=20, y=220)      
z = Entry(win, cursor="coffee_mug")
z.place(x=70, y=220)

img = PhotoImage(file = '4.png')
photo = Label(win, image=img).place(x=200, y=0)

def fact(x):
      res = 1
      for i in range(x):
            res *= (i+1)
      return res

def forming():
      global a 
      a = [[0 for i in range(9)] for j in range(9)]
            
      for i in range(1, len(a)+1):
            for j in range(1, len(a)+1):
                  if i+j > 5:
                        a[i-1][j-1] = 2*(cos((int(x.get()))-((pi)/i)))
                  else:
                        a[i-1][j-1] = 1+(int(y.get()))+(((int(z.get()))**i)/fact(i))

      f = open("file1.txt", "w")
      f.close()
      f = open("file1.txt", "a")
      for j in range(len(a)):
            strr = ""
            for i in range(len(a)):
                  strr = strr + str(a[j][i]) + " "
            strr = strr + "\n"
            f.write(strr)
      f.write("\n")
      f.close()
      
      lbl = Label(win, text="A=", cursor='spraycan')
      lbl.place(x=220, y=140)      
      x1 = 370
      y1 = 140
      for i in range(len(a)):
            x1 = 370
            for j in range(len(a[0])):
                  lbl = Label(win, text="%.3f"%a[i][j], cursor='spraycan')
                  lbl.place(x=x1, y=y1)
                  x1 += 50
            y1 += 40
      
            
b = Button(win, command=forming, text="Forming")
b.place(x=20, y=260)

def transformation():
      
      global sr
      global x
      sr = []
      x = []
      for i in range(len(a)):
            summ = 0
            for j in range(len(a)):
                  summ += a[i][j]
            sr.append(summ/len(a))
      
      for i in range(9):
            a[i][1], a[i][4] = a[i][4], a[i][1]

      strr=""
      f = open("file1.txt", "a")
      for j in range(len(sr)):
            strr = strr + str(sr[j]) + " "
      f.write(strr)
      f.write("\n")
      f.write("\n")
      strr = ""
      for j in range(len(a)):
            strr = ""
            for i in range(len(a)):
                  strr = strr + str(a[j][i]) + " "
            strr = strr + "\n"
            f.write(strr)
      f.write("\n")
      f.close()
      
      lbl = Label(win, text="Средн. знач. строк=", cursor='spraycan')
      lbl.place(x=220, y=510)
      x1 = 370
      for i in range(len(sr)):
            lbl = Label(win, text="%.3f"%sr[i], cursor='spraycan')
            lbl.place(x=x1, y=510)
            x1 += 50
      lbl = Label(win, text="Изм. A=", cursor='spraycan')
      lbl.place(x=220, y=550)
      x1 = 370
      y1 = 550
      for i in range(len(a)):
            x1 = 370
            for j in range(len(a[0])):
                  lbl = Label(win, text="%.3f" % a[i][j], cursor='spraycan')
                  lbl.place(x=x1, y=y1)
                  x1 += 50
            y1 += 40


b = Button(win, command=transformation, text="Transformation")
b.place(x=20, y=290)

def forming_x():
      for i in range(1, len(a)+1, 2):
            x.append(sr[i-1])

      strr = ""
      f = open("file1.txt", "a")
      for j in range(len(x)):
            strr = strr + str(x[j]) + " "
      f.write(strr)
      f.write("\n")
      f.write("\n")
      f.close()

      lbl = Label(win, text="X=", cursor='spraycan')
      lbl.place(x=840, y=140)
      x1 = 900
      for i in range(len(x)):
            lbl = Label(win, text="%.3f" % x[i], cursor='spraycan')
            lbl.place(x=x1, y=140)
            x1 += 50
b = Button(win, command=forming_x, text="Forming X")
b.place(x=20, y=320)
      
def transformation_x():
      for i in range(len(x)-1):
            for j in range(len(x)-i-1):
                  if x[j] > x[j+1]:
                        x[j], x[j+1] = x[j+1], x[j]

      strr = ""
      f = open("file1.txt", "a")
      for j in range(len(x)):
            strr = strr + str(x[j]) + " "
      f.write(strr)
      f.write("\n")
      f.write("\n")
      f.close()

      lbl = Label(win, text="Изм. X=", cursor='spraycan')
      lbl.place(x=840, y=170)
      x1 = 900
      for i in range(len(x)):
            lbl = Label(win, text="%.3f" % x[i], cursor='spraycan')
            lbl.place(x=x1, y=170)
            x1 += 50
b = Button(win, command=transformation_x, text="Transformation X")
b.place(x=20, y=350)

#print("\n")
#print(sr)
#print("\n")
#for i in range(len(a)):
      #print(a[i])
#print("\n")
#print(x)
#print("\n")


#transformation_x()

#for j in range(len(x)):
      #strr = strr + str(x[j]) + " "
#f.write(strr)
#f.write("\n")
#f.write("\n")
#strr = ""
#print(x)

win.mainloop()