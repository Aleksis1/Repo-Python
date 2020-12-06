# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

my_list = [True, 'ABC', 123, None]
from itertools import cycle

x = 0
for el in cycle(my_list):
    if x < 20:
        print(el)
        x += 1
    else:
        break



from itertools import count

x = 0
for el in count(int(input('Введите стартовое число: '))):
    if x < 20:
        print(el)
        x += 1
    else:
        break
