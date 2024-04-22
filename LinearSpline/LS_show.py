import numpy as np
import matplotlib.pyplot as plt
import LinearSpline as ls
from Helpers.func_dots import get_points, get_func_diff
from Helpers.funcs import f_3, f_m


"""---Выбор узлов разными способами для нашей функции---"""

# 5 узлов для линейного сплайна (получается 7 всего)
svalues_matrix_uni_5 = get_points(0, 4, 5, f_3, 'uni_spline')
svalues_matrix_opt_5 = get_points(0, 4, 5, f_3, 'opt_spline')

# 10 узлов для линейного сплайна (получается 12 всего)
svalues_matrix_uni_10 = get_points(0, 4, 10, f_3, 'uni_spline')
svalues_matrix_opt_10 = get_points(0, 4, 10, f_3, 'opt_spline')

# 25 узлов для линейного сплайна (получается 27 всего)
svalues_matrix_uni_25 = get_points(0, 4, 25, f_3, 'uni_spline')
svalues_matrix_opt_25 = get_points(0, 4, 25, f_3, 'opt_spline')

# 50 узлов для линейного сплайна (получается 52 всего)
svalues_matrix_uni_50 = get_points(0, 4, 50, f_3, 'uni_spline')
svalues_matrix_opt_50 = get_points(0, 4, 50, f_3, 'opt_spline')


"""---Линейный сплайн---"""

print("---Линейный сплайн--- \n")

fig, ax = plt.subplots(2, 2)
plt.subplots_adjust(wspace=0.3, hspace=0.3)

x = np.linspace(0, 4, 200)

"""---5 узлов---"""

lspline_opt_5 = ls.LinearSpline(5, svalues_matrix_opt_5)
lspline_uni_5 = ls.LinearSpline(5, svalues_matrix_uni_5)

ax[0, 0].set_title('5 узлов')
ax[0, 0].set_ylim([0.5, 1.7])
ax[0, 0].plot(x, lspline_uni_5(x))
ax[0, 0].plot(x, lspline_opt_5(x))
ax[0, 0].plot(x, f_3(x))
ax[0, 0].legend(['Равномерно', 'Оптимально', 'Функция'], prop={'size': 7})


print(f"---5 узлов---")
print(f"Максимальное отклонение uni: {get_func_diff(0, 4, 511, f_3, lspline_uni_5):.3f}")
print(f"Максимальное отклонение opt: {get_func_diff(0, 4, 511, f_3, lspline_opt_5):.3f}")

"""---10 узлов---"""

lspline_opt_10 = ls.LinearSpline(10, svalues_matrix_opt_10)
lspline_uni_10 = ls.LinearSpline(10, svalues_matrix_uni_10)


ax[0, 1].set_title('10 узлов')
ax[0, 1].set_ylim([0.5, 1.7])
ax[0, 1].plot(x, lspline_uni_10(x))
ax[0, 1].plot(x, lspline_opt_10(x))
ax[0, 1].plot(x, f_3(x))
ax[0, 1].legend(['Равномерно', 'Оптимально', 'Функция'], prop={'size': 7})


print(f"---10 узлов---")
print(f"Максимальное отклонение uni: {get_func_diff(0, 4, 511, f_3, lspline_uni_10):.3f}")
print(f"Максимальное отклонение opt: {get_func_diff(0, 4, 511, f_3, lspline_opt_10):.3f}")

"""---25 узлов---"""

lspline_opt_25 = ls.LinearSpline(25, svalues_matrix_opt_25)
lspline_uni_25 = ls.LinearSpline(25, svalues_matrix_uni_25)


ax[1, 0].set_title('25 узлов')
ax[1, 0].set_ylim([0.5, 1.7])
ax[1, 0].plot(x, lspline_uni_25(x))
ax[1, 0].plot(x, lspline_opt_25(x))
ax[1, 0].plot(x, f_3(x))
ax[1, 0].legend(['Равномерно', 'Оптимально', 'Функция'], prop={'size': 7})


print(f"---25 узлов---")
print(f"Максимальное отклонение uni: {get_func_diff(0, 4, 511, f_3, lspline_uni_25):.3f}")
print(f"Максимальное отклонение opt: {get_func_diff(0, 4, 511, f_3, lspline_opt_25):.3f}")

"""---50 узлов---"""

lspline_opt_50 = ls.LinearSpline(50, svalues_matrix_opt_50)
lspline_uni_50 = ls.LinearSpline(50, svalues_matrix_uni_50)


ax[1, 1].set_title('50 узлов')
ax[1, 1].set_ylim([0.5, 1.7])
ax[1, 1].plot(x, lspline_uni_50(x))
ax[1, 1].plot(x, lspline_opt_50(x))
ax[1, 1].plot(x, f_3(x))
ax[1, 1].legend(['Равномерно', 'Оптимально', 'Функция'], prop={'size': 7})


print(f"---50 узлов---")
print(f"Максимальное отклонение uni: {get_func_diff(0, 4, 511, f_3, lspline_uni_50):.3f}")
print(f"Максимальное отклонение opt: {get_func_diff(0, 4, 511, f_3, lspline_opt_50):.3f}")

plt.show()
