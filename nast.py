from scipy.special import roots_legendre
from funcs import *
import numpy as np

def gauss_quadrature(f, a, b, n):
    """
    Вычисляет интеграл функции f на интервале [a, b] 
    с использованием квадратурной формулы Гаусса-Лежандра с n узлами.
    """
    # Получаем узлы и веса Гаусса-Лежандра для заданного n
    nodes, weights = roots_legendre(n)
    
    # Преобразуем узлы из интервала [-1, 1] в [a, b]
    x_transformed = 0.5 * (b - a) * nodes + 0.5 * (a + b)

    
    # Вычисляем взвешенную сумму значений функции
    integral = 0.5 * (b - a) * sum(weights * f(x_transformed))
    
    return integral

# Пример использования
if __name__ == "__main__":
    # Пример 1: Интеграл от x^2 на [0, 2] (точное значение: 8/3 ≈ 2.6667)
    f = lambda x: np.log(1 + x) / (1 + x**2)
    a, b = 0, 1
    k = 4  # Количество узлов
    result = gauss_quadrature(f, a, b, k)
    print(f"result от {a} до {b} ≈ {result}")
    print(f"pogresnost: {abs(math.pi/8*math.log(2) - result)}")