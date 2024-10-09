import numpy as np


class QuadraticSpline():
    def __init__(self, n: int, nodes: list):
        self.n = n  # amount of nodes
        self.nodes = nodes  # nodes list

    def generate_matrix(self):
        dimension = (self.n + 1) * 3
        matrix = [[0 for i in range(dimension)] for j in range(dimension)]
        X = self.nodes[0]

        for i in range(0, dimension, 3):    # выбираем квадрат 3х3
            for j in range(3):  # идем по квадрату и заполняем значениями
                for k in range(3):
                    if j == 2:  #заполняем строчку матрицы с условием равенства производных
                        if k == 0:
                            matrix[j+i][k+i] = 2*X[i//3 + 1]
                        elif k == 1:
                            matrix[j+i][k+i] = 1    #если k=2 оставляем ноль
                    else:
                        if k == 0:
                            matrix[j+i][k+i] = X[i//3 + j]**2
                        elif k == 1:
                            matrix[j+i][k+i] = X[i//3 + j]
                        else:
                            matrix[j+i][k+i] = 1
            if i != 0:
                for j in range(3):
                    if j == 0:
                        matrix[i - 1][j + i] = -1 * 2 * X[i // 3]
                    elif j == 1:
                        matrix[i - 1][j + i] = -1

        return matrix

    def solve_matrix(self):
        matrix_x = np.array(self.generate_matrix())
        Y = []
        for i in range(self.n + 1):
            Y.append(self.nodes[1][i])
            Y.append(self.nodes[1][i+1])
            Y.append(0)
        A = np.linalg.solve(matrix_x, Y)

        return A

    def build_system(self):
        l_amount = self.n + 1   # количество линейных функций в сплайне
        S = [[], []]
        X = self.nodes[0]
        A = self.solve_matrix()

        for i in range(l_amount):
            range_tuple = tuple([X[i], X[i+1]])
            S[1].append(range_tuple)
        for i in range(0, l_amount * 3, 3):
            coeffs_tuple = tuple([A[i], A[i + 1], A[i + 2]])
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
                    return func_coeffs[i][0] * x ** 2 + func_coeffs[i][1] * x + func_coeffs[i][2]

        if isinstance(x, np.ndarray):
            Y = []
            X = set()
            j = 0
            i = 0
            while j < x.size:
                if x[j] in X:  # проверяем, что не берем одну и ту же точку два раза
                    j += 1
                while i < l_amount:
                    if np.logical_and(ranges[i][0] <= x[j], x[j] <= ranges[i][1]):
                        y = func_coeffs[i][0] * x[j] ** 2 + func_coeffs[i][1] * x[j] + func_coeffs[i][2]
                        Y.append(y)
                        X.add(x[j])
                        j += 1
                        break
                    else:
                        i += 1
            return Y
