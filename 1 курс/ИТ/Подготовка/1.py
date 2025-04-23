from random import randint

n = 6
a = [[randint(-100, 100) for j in range(n)] for i in range(n)]
print("Matrix A: ")
for i in range(n):
	print(a[i])

mx = a[0][0]
ind_i = 0
ind_j = 0
for i in range(n):
	for j in range(n):
		if mx < a[i][j]:
			mx = a[i][j]
			ind_i = i
			ind_j = j
print("\nMax element: ")
print(mx)

elems = []
k = 1
for i in range(ind_i, -1, -1):
	if (ind_i + ind_j >= n-1) and i == 0:
		break
	for j in range(ind_j+k, n):
		elems.append(a[i][j])
	k += 1

l = ind_j
if ind_i != n-1:
	for i in range(ind_i+1, n):
		l -= 1
		if (ind_i + ind_j < n-1) and l == 0:
			for j in range(l+1, n):
				elems.append(a[i][j])
			continue
		if l == -1:
			if i == n-1:
				for j in range(n):
					elems.append(a[n-1][j])
			else:
				for t in range(i, n):
					for j in range(n):
						elems.append(a[t][j])
			break
		for j in range(l+1, n):
			elems.append(a[i][j])
print(elems)