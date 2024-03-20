# Модуль с функциями, которые возвращают точки принадлежащие заданным функциям
# Если хотим выбрать равномерно mode == uni, если оптимально mode == opt

from numpy import cos
from numpy import pi


def get_points(start: int, end: int, n: int, f, mode: str) -> list:
    '''Выбрать точки (x,y), принадлежащие функции'''

    if mode == 'uni':
        '''Берем n точек на отрезке [start, end] равномерно'''

        values_matrix = [[], []]
        step = abs(end - start) / (n + 1)
        for i in range(n):
            values_matrix[0].append(start + step)
            new_value = f(start + step)
            values_matrix[1].append(new_value)
            start = start + step

        return values_matrix

    elif mode == 'opt':
        '''Берем n точек на отрезке [start, end] оптимально'''

        values_matrix = [[], []]
        for i in range(n):
            x = ((end - start) * cos(((2 * i + 1) * pi) / (2 * (n + 1))) + (end + start)) / 2
            values_matrix[0].append(x)
            values_matrix[1].append(f(x))

        return values_matrix

    else:
        '''Обработка ошибки'''

        raise Exception('try: mode == uni or mode == opt')

def get_func_diff(start, end, n, f1, f2) -> float:
    '''max|f1(x) - f2(x)| and (x, y) for each x from [start, end] with step'''

    step = abs(end - start) / (n + 1)
    max_diff = float('-inf')
    max_x = 0

    for i in range(n):
        new_value = abs(f1(start + step) - f2(start + step))
        if new_value > max_diff:
            max_diff = new_value
            max_x = start + step
        start = start + step

    return max_diff, max_x
