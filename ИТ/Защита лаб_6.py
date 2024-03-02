from random import randint
a1 = [[randint(-100, 100) for j in range(8)] for i in range(8)]
print("Матрица a1 случайных чисел: ")
for i in range(len(a1)):
    print(a1[i])
f = open("file.txt", "r")
a2 = [0 for i in range(8)]
for i in range(8):
    strr = f.readline().split()
    a2[i] = [int(strr[j]) for j in range(len(a2))]

    
def f(m):
    b = []
    for i in range(len(m)):
        summ = 0
        k = 0
        for j in range(len(m[0])):
            if m[i][j] >= 0:
                summ += m[i][j]
                k += 1
        if k != 0:
            b.append(summ/k)
        else:
            b.append(0)
    print("\nВектор b: ")
    for i in range(len(b)):
        print(f"%.3f"%b[i], " ")
    
    mn = b[0]
    ind = 0
    for i in range(len(b)):
        if b[i] < mn:
            mn = b[i]
            ind = i
    print(f"\nМинимальный элемент вектора b: %.3f"%mn)
#     for i in range(ind):
#         for j in range(ind-i):
#             if b[j] < b[j+1]:
#                 b[j], b[j+1] = b[j+1], b[j]
    
    
    for i in range(len(b)):
        for j in range(len(b)-i-1):
            if j < ind:
                if b[j] < b[j+1]:
                    b[j], b[j+1] = b[j+1], b[j]
            if j > ind:
                if b[j] > b[j+1]:
                    b[j], b[j+1] = b[j+1], b[j]
    print("\nОтсортированный вектор b: ")
    for i in range(len(b)):
        print(f"%.3f"%b[i], " ")
    
    
f(a1)
print("\nМатрица a2 считанных из файла чисел: ")
for i in range(len(a1)):
    print(a2[i])
f(a2)