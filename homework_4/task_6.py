# Реализовать два небольших скрипта:
# ● итератор, генерирующий целые числа, начиная с указанного;
# ● итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что
# создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.

from itertools import count, cycle

n = 10
num_list = [num for num in range(3)]
counter = count()
cycler = cycle(num_list)
print([next(counter) for num in range(n)])
print([next(cycler) for num in range(n)])
