from random import randint
a = [[randint(-100, 100) for i in range(5)] for j in range(5)]
mn = a[1][4]
mx = a[0][1]
k = 1
imx = 0
jmx = 1
imn = 1
jmn = 4

print("Исходная матрица: ")
for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[i][j], end="   ")
    print("")

for i in range(len(a)//2):
    for j in range(k, len(a[0])-(k-1)-1):
        if mn > a[i][j]:
            mn = a[i][j]
            imn = i
            jmn = j
    k += 1

k = 0
for i in range(1, len(a)-1):
    for j in range(len(a[0])-k-1, len(a[0])):
        if mx < a[i][j]:
            mx = a[i][j]
            imx = i
            jmx = j
    if i >= len(a)//2:
        k -= 1
    else:
        k += 1
a[imx][jmx], a[imn][jmn] = a[imn][jmn], a[imx][jmx]
print("\nИтоговая матрица: ")
for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[i][j], end="   ")
    print("")

print(f"\nМаксимальный элемент: {mx}")
print(f"\nМинимальный элемент: {mn}")