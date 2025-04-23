import random

A = []
C = [[0 for column in range(4)] for row in range(5)]
index_i = 0
index_j = 0
index_A = 0
l = 4

def creating():
	global A
	A = [random.randint(-20, 20) for element in range(20)]

creating()

def solution():
	global l

	def right(number_of_elements):
		global A, C, index_A, index_i, index_j
		for j in range(number_of_elements):
			C[index_i][index_j] = A[index_A]
			index_j += 1
			index_A += 1
		index_i += 1
		index_j -= 1

	def down(number_of_elements):
		global A, C, index_A, index_i, index_j
		for i in range(number_of_elements):
			C[index_i][index_j] = A[index_A]
			index_i += 1
			index_A += 1
		index_i -= 1
		index_j -= 1

	def left(number_of_elements):
		global A, C, index_A, index_i, index_j
		for j in range(number_of_elements):
			C[index_i][index_j] = A[index_A]
			index_j -= 1
			index_A += 1
		index_j += 1
		index_i -= 1

	def up(number_of_elements):
		global A, C, index_A, index_i, index_j
		for i in range(number_of_elements):
			C[index_i][index_j] = A[index_A]
			index_i -= 1
			index_A += 1
		index_i += 1
		index_j += 1
		
	for i in range(2):
		right(l)
		down(l)
		l -= 1
		left(l)
		up(l)
		l -= 1


print(A)

solution()
for i in range(len(C)):
	print(C[i])