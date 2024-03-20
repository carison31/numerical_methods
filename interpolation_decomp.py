import matplotlib.pyplot as plt
import numpy as np
import math


def f_4(x):
    return x**0.5 + np.cos(x)

class Lagrange_polynomial:
    def __init__(self, n: int, nodes: list):
        self.n = n  # amount of nodes
        self.nodes = nodes  # nodes list
    def __call__(self, x):
        L = 0
        X = self.nodes[0]
        Y = self.nodes[1]
        for i in range(self.n):
            denom = 1
            numer = 1
            for j in range(n):
                if i != j:
                    denom *= X[i] - X[j]
                    numer *= x - X[j]

            l = numer / denom
            L += l * Y[i]

        return L

def get_func_diff(start, end, n, f, values_matrix):
    values_diff = []
    step = abs(end - start) / (n + 1)
    for i in range(n):
        new_value = abs(lagrange_polynomial(start + step, values_matrix, 7) - f(start + step))
        values_diff.append(new_value)
        start = start + step

    return values_diff

def get_values(start, end, n, f):    # берем n точек на отрезке [start, end]
    values_matrix = [[], []]
    step = abs(end - start) / (n + 1)
    for i in range(n):
        values_matrix[0].append(start + step)
        new_value = f(start + step)
        values_matrix[1].append(new_value)
        start = start + step

    return values_matrix

def get_opt_values(start, end, n, f):
    values_matrix = [[], []]
    for i in range(n):
        x = ((end - start) * np.cos(((2*i+1)*np.pi)/(2*(n+1))) + (end+start))/2
        values_matrix[0].append(x)
        values_matrix[1].append(f(x))

    return values_matrix

def lagrange_polynomial(x, values_matrix, n):
    L = 0
    X = values_matrix[0]
    Y = values_matrix[1]
    for i in range(n):   # n - amount of known values
        denom = 1
        numer = 1
        for j in range(n):
            if i != j:
                denom *= X[i] - X[j]
                numer *= x - X[j]

        l = numer / denom
        L += l * Y[i]

    return L


fig, ax = plt.subplots()
ax.set_title('График функции 4')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

x = np.linspace(0, 15, 200)
values_matrix = get_values(0, 15, 7, f_4)
f = lagrange_polynomial(x, values_matrix, 7)
ax.plot(x, f)

x = np.linspace(0, 15, 200)
values_matrix_opt = get_opt_values(0, 15, 7, f_4)
f = lagrange_polynomial(x, values_matrix_opt, 7)
ax.plot(x, f)

h = x**0.5 + np.cos(x)
ax.plot(x, h)

plt.rc('grid', linestyle="-", color='black')
plt.grid(True)
plt.locator_params (axis='x', nbins= 15)
plt.locator_params (axis='y', nbins= 15)
plt.plot(np.array(values_matrix[0]), np.array(values_matrix[1]),'ro')
plt.plot(np.array(values_matrix_opt[0]), np.array(values_matrix_opt[1]),'bo')
ax.legend(['Равномерные точки', 'Оптимальные точки', 'Первоначальная функция', 'Равномерные точки', 'Оптимальные точки'])
plt.show()

