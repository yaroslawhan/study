from random import randint

n = 4
k = [[randint(-100, 100) for j in range(n)] for i in range(n)]
print("Matrix K: ")
for i in range(n):
	print(k[i])

x = []

for i in range(0, n-1):
	x.append(k[i][i+1])

for i in range(1, n):
	x.append(k[i][i-1])

print(x)