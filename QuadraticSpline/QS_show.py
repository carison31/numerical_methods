import numpy as np
import matplotlib.pyplot as plt
import QuadraticSpline as qs
from Helpers.func_dots import get_points, get_func_diff
from Helpers.funcs import f_3, f_m


"""---Выбор узлов разными способами для нашей функции---"""

# 5 узлов для квадратичного сплайна (получается 7 всего)
svalues_matrix_uni_5 = get_points(0, 75, 5, f_3, 'uni_spline')
svalues_matrix_opt_5 = get_points(0, 75, 5, f_3, 'opt_spline')

# 10 узлов для квадратичного сплайна (получается 12 всего)
svalues_matrix_uni_10 = get_points(0, 75, 10, f_3, 'uni_spline')
svalues_matrix_opt_10 = get_points(0, 75, 10, f_3, 'opt_spline')

# 25 узлов для квадратичного сплайна (получается 27 всего)
svalues_matrix_uni_25 = get_points(0, 75, 25, f_3, 'uni_spline')
svalues_matrix_opt_25 = get_points(0, 75, 25, f_3, 'opt_spline')

# 50 узлов для квадратичного сплайна (получается 52 всего)
svalues_matrix_uni_50 = get_points(0, 75, 50, f_3, 'uni_spline')
svalues_matrix_opt_50 = get_points(0, 75, 50, f_3, 'opt_spline')


"""---Квадратичный сплайн---"""

print("---Квадратичный сплайн--- \n")

fig, ax = plt.subplots(2, 2)
plt.subplots_adjust(wspace=0.3, hspace=0.3)

x = np.linspace(0, 75, 200)

"""---5 узлов---"""

qspline_opt_5 = qs.QuadraticSpline(5, svalues_matrix_opt_5)
qspline_uni_5 = qs.QuadraticSpline(5, svalues_matrix_uni_5)

ax[0, 0].set_title('5 узлов')
ax[0, 0].set_ylim([-2, 15])
ax[0, 0].plot(x, qspline_uni_5(x))
ax[0, 0].plot(x, qspline_opt_5(x))
ax[0, 0].plot(x, f_3(x))
ax[0, 0].legend(['Равномерно', 'Оптимально', 'Функция'], prop={'size': 7})


print(f"---5 узлов---")
print(f"Максимальное отклонение uni: {get_func_diff(0, 75, 511, f_3, qspline_uni_5):.3f}")
print(f"Максимальное отклонение opt: {get_func_diff(0, 75, 511, f_3, qspline_opt_5):.3f}")

"""---10 узлов---"""

qspline_opt_10 = qs.QuadraticSpline(10, svalues_matrix_opt_10)
qspline_uni_10 = qs.QuadraticSpline(10, svalues_matrix_uni_10)


ax[0, 1].set_title('10 узлов')
ax[0, 1].set_ylim([-2, 15])
ax[0, 1].plot(x, qspline_uni_10(x))
ax[0, 1].plot(x, qspline_opt_10(x))
ax[0, 1].plot(x, f_3(x))
ax[0, 1].legend(['Равномерно', 'Оптимально', 'Функция'], prop={'size': 7})


print(f"---10 узлов---")
print(f"Максимальное отклонение uni: {get_func_diff(0, 75, 511, f_3, qspline_uni_10):.3f}")
print(f"Максимальное отклонение opt: {get_func_diff(0, 75, 511, f_3, qspline_opt_10):.3f}")

"""---25 узлов---"""

qspline_opt_25 = qs.QuadraticSpline(25, svalues_matrix_opt_25)
qspline_uni_25 = qs.QuadraticSpline(25, svalues_matrix_uni_25)


ax[1, 0].set_title('25 узлов')
ax[1, 0].set_ylim([-2, 15])
ax[1, 0].plot(x, qspline_uni_25(x))
ax[1, 0].plot(x, qspline_opt_25(x))
ax[1, 0].plot(x, f_3(x))
ax[1, 0].legend(['Равномерно', 'Оптимально', 'Функция'], prop={'size': 7})


print(f"---25 узлов---")
print(f"Максимальное отклонение uni: {get_func_diff(0, 75, 511, f_3, qspline_uni_25):.3f}")
print(f"Максимальное отклонение opt: {get_func_diff(0, 75, 511, f_3, qspline_opt_25):.3f}")

"""---50 узлов---"""

qspline_opt_50 = qs.QuadraticSpline(50, svalues_matrix_opt_50)
qspline_uni_50 = qs.QuadraticSpline(50, svalues_matrix_uni_50)


ax[1, 1].set_title('50 узлов')
ax[1, 1].set_ylim([-2, 15])
ax[1, 1].plot(x, qspline_uni_50(x))
ax[1, 1].plot(x, qspline_opt_50(x))
ax[1, 1].plot(x, f_3(x))
ax[1, 1].legend(['Равномерно', 'Оптимально', 'Функция'], prop={'size': 7})


print(f"---50 узлов---")
print(f"Максимальное отклонение uni: {get_func_diff(0, 75, 511, f_3, qspline_uni_50):.3f}")
print(f"Максимальное отклонение opt: {get_func_diff(0, 75, 511, f_3, qspline_opt_50):.3f}")

plt.show()
