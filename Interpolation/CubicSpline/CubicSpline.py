import numpy as np

class CubicSpline():
    def __init__(self, n: int, nodes: list):
        self.n = n  # amount of nodes
        self.nodes = nodes  # nodes list

    def generate_matrix(self):
        dimension = (self.n)
        matrix = [[0 for i in range(dimension)] for j in range(dimension)]
        X = self.nodes[0]

        for i in range(0, dimension):
            matrix[i][i] = 2*(X[i+2] - X[i])
            if i == dimension - 1:
                break
            matrix[i][i+1] = X[i+1] - X[i]
            matrix[i+1][i] = X[i+1] - X[i]
        return matrix

    def free_coeffs(self):
        X = self.nodes[0]
        Y = self.nodes[1]
        dimension = self.n + 2
        free_list = []

        for i in range(1, dimension - 1):
            y = 6*((Y[i+1] - Y[i]) / (X[i+1] - X[i]) - (Y[i] - Y[i-1]) / (X[i] - X[i-1]))
            free_list.append(y)

        return free_list

    def solve_matrix(self):
        matrix_x = np.array(self.generate_matrix())
        Y = self.free_coeffs()

        x = np.array(0)
        x = np.append(x, np.linalg.solve(matrix_x, Y))
        x = np.append(x, 0)

        return x

    def y_diff(self):
        y_diff2 = self.solve_matrix()
        Y = self.nodes[1]
        X = self.nodes[0]
        y_diff1 = []
        dim = self.n + 2

        for i in range(dim - 1):
            h = (X[i+1] - X[i])
            y = (Y[i+1] - Y[i]) / h - (y_diff2[i+1] * h / 6) - (y_diff2[i] * h / 3)
            y_diff1.append(y)

        return y_diff1

    def build_system(self):
        l_amount = self.n + 1
        S = [[], []]
        X = self.nodes[0]
        Y = self.nodes[1]
        y_diff1 = self.y_diff()
        y_diff2 = self.solve_matrix()

        for i in range(l_amount):
            range_tuple = tuple([X[i], X[i+1]])
            S[1].append(range_tuple)
        for i in range(l_amount):
            h = (X[i + 1] - X[i])
            coeffs_tuple = tuple([Y[i], y_diff1[i], y_diff2[i] / 2, (y_diff2[i+1] - y_diff2[i]) / (6*h) , X[i]])
            S[0].append(coeffs_tuple)

        return S

    def __call__(self, x):
        spline_system = self.build_system()
        ranges = spline_system[1]
        func_coeffs = spline_system[0]
        l_amount = self.n + 1

        if isinstance(x, float) or isinstance(x, int):
            for i in range(l_amount):
                if np.logical_and(ranges[i][0] <= x, x <= ranges[i][1]):
                    func_value = func_coeffs[i][0] \
                                 + func_coeffs[i][1] * (x - func_coeffs[i][4]) \
                                 + func_coeffs[i][2] * (x - func_coeffs[i][4]) ** 2 \
                                 + func_coeffs[i][3] * (x - func_coeffs[i][4]) ** 3
                    return func_value
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
                        y = func_coeffs[i][0] \
                                 + func_coeffs[i][1] * (x[j] - func_coeffs[i][4]) \
                                 + func_coeffs[i][2] * (x[j] - func_coeffs[i][4]) ** 2 \
                                 + func_coeffs[i][3] * (x[j] - func_coeffs[i][4]) ** 3
                        Y.append(y)
                        X.add(x[j])
                        j += 1
                        break
                    else:
                        i += 1
            return Y
