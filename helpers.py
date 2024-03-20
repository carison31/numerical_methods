import numpy as np




"""СОЗДАТЬ КЛАСС ПОЛИНОМОВ L(x) ЧТОБЫ КИДАТЬ ОБЪЕКТ В ФУНКЦИЮ"""


def get_func_diff(start, end, n, f, values_matrix):
    '''[start, end] - отрезок; n - разбиение отрезка, f - ф-ия с которой сравниваем L(x), values_matrix - таблица
    значений для построения L(x)'''
    values_diff = []
    step = abs(end - start) / (n + 1)
    for i in range(n):
        new_value = abs(lagrange_polynomial(start + step, values_matrix, b) - f(start + step))
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