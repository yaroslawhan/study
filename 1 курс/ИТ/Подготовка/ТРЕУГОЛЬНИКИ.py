from random import randint
import tkinter as tk

win = tk.Tk()
win.title('test')
win.geometry('500x500')
#n = int(input('Введите n: '))
nn = tk.Entry()
nn.place(x=0, y=0)
n = 5
a = [[randint(-100, 100) for j in range(n)] for i in range(n)]
#print(f'{a[0]}\n{a[1]}\n{a[2]}\n{a[3]}\n{a[4]}\n')
#stra = ''
#for i in range(n):
    #for j in range(n):
        #stra += str(a[i][j]) + ' '
    #stra += '\n'
strr = ''
x1 = 100
y1 = 0
stral = tk.Label(win, text='исходная матрица: ').place(x=x1, y=y1)
y1 += 30
for i in range(n):
    for j in range(n):
        stral = tk.Label(win, text=str(a[i][j])).place(x=x1, y=y1)
        x1 += 30
    y1 += 30
    strr = ''
    x1 = 100
cel = n
left = 0
right = n
temp = 0

if n%2!=0:
    for k in range(n):
        if cel == 1:
            if k+1 > n//2 + 1:
                for f in range(n-1):
                    for i in range(left, right-f-1):
                        if a[i][k] < a[i+1][k]:
                            temp = a[i][k]
                            a[i][k] = a[i+1][k]
                            a[i+1][k] = temp
                left -= 1
                right += 1               
            else:
                left -= 1
                right += 1
        else:
            for f in range(n-1):
                for i in range(left, right-f-1):
                    if a[i][k] < a[i+1][k]:
                        temp = a[i][k]
                        a[i][k] = a[i+1][k]
                        a[i+1][k] = temp
            left += 1
            right -= 1
            cel -= 2
            #print(a)
#else:
    
#print(f'{a[0]}\n{a[1]}\n{a[2]}\n{a[3]}\n{a[4]}\n')
y1 += 50
stral = tk.Label(win, text='обработанная матрица: ').place(x=x1, y=y1)
y1 += 30
for i in range(n):
    for j in range(n):
        stral = tk.Label(win, text=str(a[i][j])).place(x=x1, y=y1)
        x1 += 30
    y1 += 30
    strr = ''
    x1 = 100
win.mainloop()