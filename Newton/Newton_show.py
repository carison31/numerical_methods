import numpy as np
import matplotlib.pyplot as plt
import Newtone as newt
from func_dots import get_points, get_func_diff
from funcs import f_3, f_m


"""---Выбор узлов разными способами для нашей функции---"""

# 5 узлов
values_matrix_uni_5 = get_points(0, 75, 5, f_3, 'uni')
values_matrix_opt_5 = get_points(0, 75, 5, f_3, 'opt')

# 10 узлов
values_matrix_uni_10 = get_points(0, 75, 10, f_3, 'uni')
values_matrix_opt_10 = get_points(0, 75, 10, f_3, 'opt')

# 25 узлов
values_matrix_uni_25 = get_points(0, 75, 25, f_3, 'uni')
values_matrix_opt_25 = get_points(0, 75, 25, f_3, 'opt')

# 50 узлов
values_matrix_uni_50 = get_points(0, 75, 50, f_3, 'uni')
values_matrix_opt_50 = get_points(0, 75, 50, f_3, 'opt')

"""---Интерполяционный полином Ньютона---"""

print("---Интерполяционный полином Ньютона--- \n")

fig, ax = plt.subplots(2, 2)
plt.subplots_adjust(wspace=0.3, hspace=0.3)

x = np.linspace(0, 75, 200)

"""---5 узлов---"""

N_opt_5 = newt.NewtonePolynomial(5, values_matrix_opt_5)
N_uni_5 = newt.NewtonePolynomial(5, values_matrix_uni_5)

ax[0, 0].set_title('5 узлов')
ax[0, 0].set_ylim([-2, 15])
ax[0, 0].plot(x, N_uni_5(x))
ax[0, 0].plot(x, N_opt_5(x))
ax[0, 0].plot(x, f_3(x))
ax[0, 0].legend(['Равномерно', 'Оптимально', 'Функция'], prop={'size': 7})

print(f"---5 узлов---")
print(f"Максимальное отклонение uni: {get_func_diff(0, 75, 511, f_3, N_uni_5):.3f}")
print(f"Максимальное отклонение opt: {get_func_diff(0, 75, 511, f_3, N_opt_5):.3f}")

"""---10 узлов---"""

N_opt_10 = newt.NewtonePolynomial(10, values_matrix_opt_10)
N_uni_10 = newt.NewtonePolynomial(10, values_matrix_uni_10)


ax[0, 1].set_title('10 узлов')
ax[0, 1].set_ylim([-2, 15])
ax[0, 1].plot(x, N_uni_10(x))
ax[0, 1].plot(x, N_opt_10(x))
ax[0, 1].plot(x, f_3(x))
ax[0, 1].legend(['Равномерно', 'Оптимально', 'Функция'], prop={'size': 7})

print(f"---10 узлов---")
print(f"Максимальное отклонение uni: {get_func_diff(0, 75, 511, f_3, N_uni_10):.3f}")
print(f"Максимальное отклонение opt: {get_func_diff(0, 75, 511, f_3, N_opt_10):.3f}")

"""---25 узлов---"""

N_opt_25 = newt.NewtonePolynomial(25, values_matrix_opt_25)
N_uni_25 = newt.NewtonePolynomial(25, values_matrix_uni_25)


ax[1, 0].set_title('25 узлов')
ax[1, 0].set_ylim([-2, 15])
ax[1, 0].plot(x, N_uni_25(x))
ax[1, 0].plot(x, N_opt_25(x))
ax[1, 0].plot(x, f_3(x))
ax[1, 0].legend(['Равномерно', 'Оптимально', 'Функция'], prop={'size': 7})

print(f"---25 узлов---")
print(f"Максимальное отклонение uni: {get_func_diff(0, 75, 511, f_3, N_uni_25):.3f}")
print(f"Максимальное отклонение opt: {get_func_diff(0, 75, 511, f_3, N_opt_25):.3f}")

"""---50 узлов---"""

N_opt_50 = newt.NewtonePolynomial(50, values_matrix_opt_50)
N_uni_50 = newt.NewtonePolynomial(50, values_matrix_uni_50)


ax[1, 1].set_title('50 узлов')
ax[1, 1].set_ylim([-2, 15])
ax[1, 1].plot(x, N_uni_50(x))
ax[1, 1].plot(x, N_opt_50(x))
ax[1, 1].plot(x, f_3(x))
ax[1, 1].legend(['Равномерно', 'Оптимально', 'Функция'], prop={'size': 7})

print(f"---50 узлов---")
print(f"Максимальное отклонение uni: {get_func_diff(0, 75, 511, f_3, N_uni_50):.3f}")
print(f"Максимальное отклонение opt: {get_func_diff(0, 75, 511, f_3, N_opt_50):.3f}")

plt.show()
