import matplotlib.pyplot as plt
dots = [[1, 3], [4.5, 5], [7.5, 4], [9, 3], [6, 1], [5, 3], [7, 3]]
xses = [dots[i][0] for i in range(len(dots))]
ys = [dots[i][1] for i in range(len(dots))]

plt.scatter(xses, ys)
plt.show()