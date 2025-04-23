import numpy as np
import sympy as sp

class NonLinearEquationSolve:
	def __init__(self, right, left, eps):

		self.right = right
		self.left = left
		self.eps = eps

	def f(self, x):
		return x**3 - 12*x - 10

	def chords_and_tangents(self):

		x = sp.symbols('x', Real=True)
		first_derivative = sp.diff(self.f(x), x)
		second_derivative = sp.diff(first_derivative, x)

		iter_num = 0

		x1 = self.right
		x2 = self.left
		x1_values = [] 
		x2_values = []

		if self.f(self.right) * self.f(self.left) < 0:
			while abs(x1 - x2) > self.eps:
				if self.f(self.right)*second_derivative.subs(x, self.right) > 0:

					x1 += self.f(x1) / second_derivative.subs(x, x1)
					x2 = x1 - (self.f(x1) * (x2 - x1)) / (self.f(x2) - self.f(x1))
					x1_values.append(x1)
					x2_values.append(x2)

					iter_num += 1

				if self.f(self.left)*second_derivative.subs(x, self.left) > 0:

					x1 = x1 - (self.f(x1) * (x2 - x1)) / (self.f(x2) - self.f(x1))
					x2 = x2 - self.f(x2) / second_derivative.subs(x, x2)
					x1_values.append(x1)
					x2_values.append(x2)

					iter_num += 1

		if len(x1_values) > 10:
			x1_values = x1_values[len(x1_values) - 9::]
		if len(x2_values) > 10:
			x2_values = x2_values[len(x2_values) - 9::]

		return [(x1 + x2) / 2, x1_values, x2_values, iter_num]