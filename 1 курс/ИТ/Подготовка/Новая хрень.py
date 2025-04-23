from random import randint

n = 25
a = [randint(-100, 100) for i in range(n)]
print("Matrix A: ")
print(a)

ind_i = 2
ind_j = 2
elem = 0
c = [[0 for j in range(5)] for i in range(5)]

def up(x):
	global c
	global ind_i
	global ind_j
	global elem
	for i in range(x):
		ind_i -= 1
		c[ind_i][ind_j] = a[elem]
		elem += 1

def down(x):
	global c
	global ind_i
	global ind_j
	global elem
	for i in range(x):
		ind_i += 1
		c[ind_i][ind_j] = a[elem]
		elem += 1

def left(x):
	global c
	global ind_i
	global ind_j
	global elem
	for i in range(x):
		ind_j -= 1
		c[ind_i][ind_j] = a[elem]
		elem += 1

def right(x):
	global c
	global ind_i
	global ind_j
	global elem
	for i in range(x):
		ind_j += 1
		c[ind_i][ind_j] = a[elem]
		elem += 1

def forming():
	global c
	global ind_i
	global elem
	c[ind_i][ind_j] = a[elem]
	elem += 1
	down(2)
	right(2)
	up(4)
	left(4)
	down(4)
	right(1)
	up(3)
	right(2)
	down(2)
forming()

print("Matrix C: ")
for i in range(5):
	print(c[i])