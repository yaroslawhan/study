import random

N = 5
A = [[random.randint(-50,50) for column in range(N)] for row in range(N)]

for i in range(N):
	print(A[i])

n = 3
start_i = 2
start_j = 2
elems = []

while len(elems) < n**2:
	for i in range(n):
		for j in range(n):
			if (abs(i - start_i) < 2) or (abs(j - start_j) < 2):
				elems.append(A[i][j])

print(elems)
