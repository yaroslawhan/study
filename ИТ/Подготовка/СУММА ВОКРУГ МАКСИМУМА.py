from random import randint

a = [[randint(-100, 100) for j in range(8)] for i in range(6)]
ind_i = 0
ind_j = 0
summ = 0

print("Matrix A: ")
for i in range(6):
	print(a[i])

a_sorted = []
for i in range(6):
	for j in range(8):
		a_sorted.append(a[i][j])

print("\n", a_sorted)
for i in range(47):
	for j in range(46-i):
		if a_sorted[j] < a_sorted[j+1]:
			a_sorted[j], a_sorted[j+1] = a_sorted[j+1], a_sorted[j]

print("\n", a_sorted)

for i in range(6):
	for j in range(8):
		if a_sorted[1] == a[i][j]:
			ind_i = i
			ind_j = j

for i in range(6):
	for j in range(8):
		if (((abs(ind_i-i) == 1) and (abs(ind_j-j) == 1)) or ((ind_i == i) and (abs(ind_j-j) == 1)) or ((abs(ind_i-i) == 1) and (abs(ind_j-j) == 0))):
			summ += a[i][j]
			print(a[i][j])

print(summ)