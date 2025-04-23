from random import randint

n = 6
b = [[randint(-100, 100) for i in range(n)] for j in range(n)]
print("Matrix B: ")
for i in range(n):
	print(b[i])

temp = []
res = []
k = 0

for i in range(n//2):
	for j in range(k, n-k):
		if (b[i][j] in temp) and (b[i][j] not in res):
			res.append(b[i][j])
		temp.append(b[i][j])
	k += 1

k -= 1
for i in range(n//2, n):
	for j in range(k, n-k):
		if (b[i][j] in temp) and (b[i][j] not in res):
			res.append(b[i][j])
		temp.append(b[i][j])
	k -= 1

print("\n", temp)
print(res)