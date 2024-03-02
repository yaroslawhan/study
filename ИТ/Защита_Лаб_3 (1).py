from random import *
x = []
for i in range(15):
    x.append(randrange(-100, 101))
mx = x[0]
print(x)
for i in range(len(x)):
    if mx < x[i]:
        mx = x[i]
print(f"max = {mx}")
for i in range(len(x)):
    if x[i] == mx:
        if i == len(x)-1:
            print("Чисел после максимального элемента нет")
            break
        print(f"{len(x[i+1:])} чисел после максимального элемента")
        break