from random import randint
x = [randint(-100, 100) for i in range(8)]
y = [randint(-100, 100) for i in range(9)]
print(f"Массив x: {x}")
print(f"Массив y: {y}")
def func(a):
    k = 0
    c = 0
    for i in range(len(a)):
        if a[i] > 0:
            k += 1
        if k >= 2:
            c += 1
    if c-1 == 0:
        return 'нет элементов'
    if c == 0:
        return "в массиве менье 2-х положит. чисел"
    else:
        return c-1
print(f"Количество элементов правее 2-го положит. числа массива x: {func(x)}")
print(f"Количество элементов правее 2-го положит. числа массива y: {func(y)}")