import math
from tabulate import tabulate
from funcs import *

a = 0
b = 1


f = [(trap, 1), (simpson, 3)]


tables = [[], []]

for j in range(len(f)):
    i_past = 0
    epsilon = 10 ** -7
    h = (b - a) / 2
    r = math.inf
    n = 2
    while abs(r) >= epsilon:
        i = f[j][0](a, b, h, n)
        if i_past != 0:
            r = (i - i_past) / (2 ** (f[j][1] + 1))
        tables[j].append([f"kf{j + 1}", f"N = {n}", f"h = {h}", f"Q_h = {i}", f"R = {abs(r)}" if i_past != 0 else "-"])
        i_past = i
        n *= 2
        h /= 2

print(tabulate(tables[0], headers=["Квадратурная формула", "Число разбиений", "Шаг", "Приближённое значение интеграла", "Оценка погрешности"]))
print()
print(tabulate(tables[1], headers=["Квадратурная формула", "Число разбиений", "Шаг", "Приближённое значение интеграла", "Оценка погрешности"]))