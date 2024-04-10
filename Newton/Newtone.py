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
