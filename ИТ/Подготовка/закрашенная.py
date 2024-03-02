import random

# A = [[random.randint(-30,30) for column in range(6)] for row in range(6)]
A = [[23, -26, 25, 18, -30, 3],
	[10, 10, -13, -18, -13, -27],
	[28, 24, -15, -23, -18, -5],
	[13, -18, 3, -23, 30, 25],
	[-25, 18, 18, -4, 18, 15],
	[27, -25, 6, -28, -21, 7]]
elems = []
C = []

index_i_max, index_j_max = 0, 0
index_i_min, index_j_min = 0, 0

for i in range(6):
	for j in range(i+1):
		if A[i][j] > 0:
			elems.append(A[i][j])

maxx, minn = elems[0], elems[0]

for z in range(len(elems)):
	if elems[z] > maxx:
		maxx = elems[z]
	if elems[z] < minn:
		minn = elems[z]

for i in range(6):
	for j in range(6):
		if A[i][j] == maxx:
			index_i_max, index_j_max = i, j
		if A[i][j] == minn:
			index_i_min, index_j_min = i, j

first = 0
for i in range(6):
	for j in range(6):
		

print(index_i_max, index_j_max)
print(index_i_min, index_j_min)
print(C)


