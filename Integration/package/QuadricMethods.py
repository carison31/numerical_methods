class Quadric:
    """Класс квадратурных методов интегрирования"""
    def left_rectangle(f, a, b, n):
        """Левый прямоугольник"""
        h = (b - a) / n
        integral = 0

        for i in range(n):
            integral += f(a + i * h)
        integral *= h

        return integral
    
    def middle_rectangle(f, a, b, n):
        """Серединный прямоугольник"""
        h = (b - a) / n
        integral = 0

        for i in range(n):
            integral += f(a + (i + 0.5) * h)
        integral *= h

        return integral

    def trapezoidal(f, a, b, n):
        """Методом трапеций"""
        h = (b - a) / n
        integral = 0

        for i in range(n):
            integral += f(a + i * h) + f(a + (i + 1) * h)
        integral *= h / 2

        return integral

    def simpsons(f, a, b, n):
        """Метод Симпсона"""
        if n % 2 == 1:
            n += 1
        
        h = (b - a) / n
        integral = f(a) + f(b)

        for i in range(1, n, 2):
            integral += 4 * f(a + i * h)
        
        for i in range(2, n-1, 2):
            integral += 2 * f(a + i * h)
        
        return (h / 3) * integral
