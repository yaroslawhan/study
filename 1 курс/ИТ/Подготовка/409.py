from random import randint

n = 6
#a = [[randint(-100, 100) for j in range(n)] for i in range(n)]
a = [[-84, -42, -22, 45, -66, 45],
[-27, 1, 11, 69, 23, -10],
[-57, 67, -1, -12, 82, 34],
[-30, 66, -45, 26, 28, -77],
[-21, 55, 73, -52, 74, 78],
[-95, 17, -30, 0, -62, 76]]
print("Matrix A: ")
for i in range(n):
	print(a[i])

ind_min_i = 0
ind_min_j = 0
ind_max_i = 0
ind_max_j = 0
k = 0

for j in range(n):
	for i in range(k, n):
		if a[i][j] > 0:
			mn = a[i][j]
			mx = a[i][j]
	k += 1

c = []
k = 0

for j in range(n):
	for i in range(k, n):
		if a[i][j] > 0:
			if mn > a[i][j]:
				mn = a[i][j]
				ind_min_i = i
				ind_min_j = j
			if mx < a[i][j]:
				mx = a[i][j]
				ind_max_i = i
				ind_max_j = j
	k += 1
if a[n-1][n-1] > 0:
	if mn > a[n-1][n-1]:
		mn = a[n-1][n-1]
		ind_min_i = n-1
		ind_min_j = n-1
	if mx < a[n-1][n-1]:
		mx = a[n-1][n-1]
		ind_max_i = n-1
		ind_max_j = n-1

if ind_max_i < ind_min_i:
	#1
	bol = True
	for i in range(ind_max_i, ind_min_i+1):
		if bol == True:
			for j in range(ind_max_j+1, n):
				c.append(a[i][j])
			bol = False
		else:
			if i == ind_min_i:
				for j in range(0, ind_min_j):
					c.append(a[i][j])
			else:	
				for j in range(0, n):
					c.append(a[i][j])


if ind_max_i == ind_min_i:
	if ind_max_j < ind_min_j:
		#1
		if ind_max_j+1 == ind_min_j:
			print("There's no elements")
		else:
			for j in range(ind_max_j+1, ind_min_j):
				c.append(a[i][j])

	if ind_max_j > ind_min_j:
		#2
		if ind_min_j+1 == ind_max_j:
			print("There's no elements")
		else:
			for j in range(ind_min_j+1, ind_max_j):
				c.append(a[i][j])

	if ind_max_j == ind_min_j:
		print("There's no elements")
if ind_max_i > ind_min_i:
	#2
	bol = True
	for i in range(ind_min_i, ind_max_i+1):
		if bol == True:
			for j in range(ind_min_j+1, n):
				c.append(a[i][j])
			bol = False
		else:
			if i == ind_max_i:
				for j in range(0, ind_max_j):
					c.append(a[i][j])
			else:	
				for j in range(0, n):
					c.append(a[i][j])

print("\n", mn, mx)
print(ind_min_i, ind_min_j, ind_max_i, ind_max_j)
print(c)