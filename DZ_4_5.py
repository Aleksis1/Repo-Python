# Список четных чисел от 100 до 1000 (включая границы).
# Подсказка: использовать функцию reduce().

from functools import reduce


def my_func(el_p, el):
    return el_p * el


print(f'Список четных значений: {[el for el in range(100, 1000) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка: {reduce(my_func, [el for el in range(100, 1000) if el % 2 == 0])}')
