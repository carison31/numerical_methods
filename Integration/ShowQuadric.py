from package import *

def main():
    n_values = [n for n in range(15, 1006, 10)]
    table_head = ["Разбиений", "Левые прям-ки", "Серединные прям-ки", "Трапеции", "Симпсона"]
    table = PrettyTable()
    table.field_names = table_head
    a, b = 0.1, 2.3
    lib_val, lib_err = quad(f, a, b)

    """---Заполняем таблицу значениями---"""
    for n in n_values:
        row = [n]
        row.append(f"{Quadric.left_rectangle(f, a, b, n):.5f}")
        row.append(f"{Quadric.middle_rectangle(f, a, b, n):.5f}")
        row.append(f"{Quadric.trapezoidal(f, a, b, n):.5f}")
        row.append(f"{Quadric.simpsons(f, a, b, n):.5f}")
        table.add_row(row)

    print(table)


    """---Погрешность---"""
    plt.figure(figsize=(10, 6))

    y1 = [func_error(lib_val, Quadric.left_rectangle(f, a, b, n)) for n in n_values]
    y2 = [func_error(lib_val, Quadric.middle_rectangle(f, a, b, n)) for n in n_values]
    y3 = [func_error(lib_val, Quadric.trapezoidal(f, a, b, n)) for n in n_values]
    y4 = [func_error(lib_val, Quadric.simpsons(f, a, b, n)) for n in n_values]
    plt.plot(n_values, y1, label='Левые прям-ки', color='blue')
    plt.plot(n_values, y2, label='Серединные прям-ки', color='red')
    plt.plot(n_values, y3, label='Трапеции', color='green')
    plt.plot(n_values, y4, label='Симпсона', color='purple')
    
    plt.xlabel('n')
    plt.ylabel('error')

    plt.legend("fdgdfgdfg")
    plt.show()

if __name__ == "__main__":
    main()