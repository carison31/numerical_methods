from scipy.linalg import solve
import numpy as np


class LinearSpline():
    def __init__(self, n: int, nodes: list):
        self.n = n  # amount of nodes
        self.nodes = nodes  # nodes list

    def generate_matrix(self):
        dimension = (self.n + 1) * 2
        matrix = [[0 for i in range(dimension)] for j in range(dimension)]
        X = self.nodes[0]

        for i in range(0, dimension, 2):    # выбираем квадрат 2х2
            for j in range(2):  # идем по квадрату и заполняем значениями
                for k in range(2):
                    if k == 0:
                        if j == 0:
                            matrix[j+i][k+i] = X[int(i/2)]
                        else:
                            matrix[j+i][k+i] = X[i//2 + 1]
                    else:
                        matrix[j+i][k+i] = 1

        return matrix

    def solve_matrix(self):
        matrix_x = np.array(self.generate_matrix())
        Y = []
        for i in range(self.n + 1):
            Y.append(self.nodes[1][i])
            Y.append(self.nodes[1][i+1])
        A = np.linalg.solve(matrix_x, Y)

        return A

    def build_system(self):
        l_amount = self.n + 1   # количество линейных функций в сплайне
        S = [[], []]
        X = self.nodes[0]
        A = self.solve_matrix()

        for i in range(l_amount):
            i_ = i
            if i % 2 != 0:
                i_ = i + 1
            range_tuple = tuple([X[i], X[i+1]])
            S[1].append(range_tuple)
            coeffs_tuple = tuple([A[i_], A[i_+1]])
            S[0].append(coeffs_tuple)

        return S

    def __call__(self, x):  # метод, благодаря которому объект класса есть функция
        spline_system = self.build_system()
        ranges = spline_system[1]
        func_coeffs = spline_system[0]
        l_amount = self.n + 1

        if isinstance(x, float) or isinstance(x, int):
            for i in range(l_amount):
                if np.logical_and(ranges[i][0] <= x, x <= ranges[i][1]):
                    return func_coeffs[i][0] * x + func_coeffs[i][1]

        if isinstance(x, np.ndarray):
            Y = []
            for j in range(x.size):
                for i in range(l_amount):
                    if x[j] in self.nodes[0]:
                        y = func_coeffs[i][0] * x[j] + func_coeffs[i][1]
                        Y.append(y)
                        break
                    elif np.logical_and(ranges[i][0] <= x[j], x[j] <= ranges[i][1]):
                        y = func_coeffs[i][0] * x[j] + func_coeffs[i][1]
                        Y.append(y)
            return Y

