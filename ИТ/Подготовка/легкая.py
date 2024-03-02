import random

K = []
A = []

def matrix_creating():
	global K
	K = [[random.randint(-50,50) for element in range(7)] for element in range(7)]

def procedure():
	global K, A
	for i in range(1, 8):
		for j in range(1, 8):
			if ((i + j) % 2 == 0) and (K[i-1][j-1] % 2 != 0):
				A.append(K[i-1][j-1])

matrix_creating()
procedure()

A_ascend = []
A_descend = []

print('created: ', A)

for i in range(len(A)):
	A_ascend.append(A[i])
	A_descend.append(A[i])

for i in range(len(A_ascend)):
	smallest = i
	biggest = i
	for j in range(i, len(A_ascend)):
		if A_ascend[j] < A_ascend[smallest]:
			smallest = j
		if A_descend[j] > A_descend[biggest]:
			biggest = j
	A_ascend[i], A_ascend[smallest] = A_ascend[smallest], A_ascend[i]
	A_descend[i], A_descend[biggest] = A_descend[biggest], A_descend[i]

min_ind = A.index(A_ascend[0])
max_ind = A.index(A_descend[2])

A[min_ind], A[max_ind] = A[max_ind], A[min_ind]


print('ascend: ', A_ascend)
print('descend: ', A_descend)
print('new: ', A)

