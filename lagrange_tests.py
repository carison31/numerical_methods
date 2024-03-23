import numpy as np
import matplotlib.pyplot as plt
from func_dots import get_points, get_func_diff
from funcs import f_3, f_m
from scipy.linalg import solve


'''
СДЕЛАТЬ: 
1. МОДУЛЬ С ПЛОТОМ 
'''


class LagrangePolynomial:
    '''Класс полиномов Ланранжа, проходящих через заданные точки'''
    def __init__(self, n: int, nodes: list):
        self.n = n  # amount of nodes
        self.nodes = nodes  # nodes list

    def __call__(self, x):  # метод, благодаря которому объект класса есть функция
        L = 0
        X = self.nodes[0]
        Y = self.nodes[1]
        for i in range(self.n):
            denom = 1
            numer = 1
            for j in range(self.n):
                if i != j:
                    denom *= X[i] - X[j]
                    numer *= x - X[j]

            l = numer / denom
            L += l * Y[i]

        return L


class NewtonePolynomial:
    '''Класс полиномов Ньютона, проходящих через заданные точки'''
    def __init__(self, n: int, nodes: list):
        self.n = n  # amount of nodes
        self.nodes = nodes  # nodes list

    def divided_diffs(self, n: int):
        X = self.nodes[0]
        Y = self.nodes[1]
        N = 0

        for i in range(n):
            elem = Y[i]
            for j in range(n):
                if i != j:
                    diff = X[i] - X[j]
                    elem /= diff
            N += elem

        return N

    def __call__(self, x):  # метод, благодаря которому объект класса есть функция
        N = self.divided_diffs(1)
        X = self.nodes[0]

        for i in range(2, self.n + 1):
            elem = self.divided_diffs(i)
            for j in range(i - 1):
                elem *= x - X[j]
            N += elem

        return N

class LinearSpline():
    def __init__(self, n: int, nodes: list):
        self.n = n  # amount of nodes
        self.nodes = nodes  # nodes list

    def generate_matrix(self):
        dimension = (self.n - 1) * 2
        matrix = [[0 for i in range(dimension)] for j in range(dimension)]
        X = self.nodes[0]

        for i in range(0, dimension, 2):    # выбираем квадрат 2х2
            for j in range(2):  # идем по квадрату и заполняем значениями
                for k in range(2):
                    if k == 0:
                        if j == 0:
                            matrix[j+i][k+i] = X[int(i/2)]
                        else:
                            matrix[j+i][k+i] = 1
                    else:
                        if j == 0:
                            matrix[j+i][k+i] = X[i//2 + 1]
                        else:
                            matrix[j+i][k+i] = 1

        return matrix

    # def __call__(self, x):  # метод, благодаря которому объект класса есть функция


fig, ax = plt.subplots()
ax.set_title('График функции 4')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

values_matrix_uni = get_points(0, 15, 7, f_3, 'uni')
values_matrix_opt = get_points(0, 15, 7, f_3, 'opt')
'''
N = NewtonePolynomial(7, values_matrix_opt)
x = np.linspace(0, 15, 200)
ax.plot(x, N(x))
'''
L_uni = LagrangePolynomial(7, values_matrix_uni)
x = np.linspace(0, 15, 200)
ax.plot(x, L_uni(x))
"""
L_opt = LagrangePolynomial(3, values_matrix_opt)
x = np.linspace(0, 15, 200)
ax.plot(x, L_opt(x))
"""
ax.plot(x, f_3(x))



plt.rc('grid', linestyle="-", color='black')
plt.grid(True)
plt.locator_params (axis='x', nbins= 15)
plt.locator_params (axis='y', nbins= 15)
plt.plot(np.array(values_matrix_uni[0]), np.array(values_matrix_uni[1]),'ro')
#plt.plot(np.array(values_matrix_opt[0]), np.array(values_matrix_opt[1]),'bo')
# ax.legend(['Ньютон', 'Равномерные точки', 'Оптимальные точки', 'Первоначальная функция', 'Равномерные точки', 'Оптимальные точки'])
plt.show()

print(get_func_diff(values_matrix_opt[0][-1], values_matrix_opt[0][0], 100, f_3, L_uni))
#print(get_func_diff(values_matrix_opt[0][-1], values_matrix_opt[0][0], 100, f_3, L_opt))
"""СДЕЛАТЬ НОРМ ВВОД АРГУМЕНТОВ В GET FUNC DIFF
СДЕЛАТЬ НОРМ НЕСКОЛЬКО ГРАФИКОВ"""
# print(values_matrix_opt[0])
test_nodes = [[0, 2, 3], [1, 3, 2]]
LS = LinearSpline(3, test_nodes)
m = LS.generate_matrix()
print(m)