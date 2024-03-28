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