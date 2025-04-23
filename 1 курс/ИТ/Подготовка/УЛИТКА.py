from random import randint

n = 25
c = [randint(-100, 100) for i in range(n)]
print("Matrix C: ")
print(c)

ind_i = 2
ind_j = 2
elem = 0
a = [[0 for i in range(5)] for j in range(5)]
k = 1

def up(x):
	global ind_i
	global ind_j
	global elem
	for i in range(x):
		ind_i -= 1
		a[ind_i][ind_j] = c[elem]
		elem += 1

def down(x):
	global ind_i
	global ind_j
	global elem
	for i in range(x):
		ind_i += 1
		a[ind_i][ind_j] = c[elem]
		elem += 1

def left(x):
	global ind_i
	global ind_j
	global elem
	for i in range(x):
		ind_j -= 1
		a[ind_i][ind_j] = c[elem]
		elem += 1

def right(x):
	global ind_i
	global ind_j
	global elem
	for i in range(x):
		ind_j += 1
		a[ind_i][ind_j] = c[elem]
		elem += 1

a[ind_i][ind_j] = c[elem]
elem += 1
for g in range(2):
	right(k)
	down(k)
	k += 1
	left(k)
	up(k)
	k += 1

right(4)
print("Matrix A: ")
for i in range(5):
	print(a[i])
