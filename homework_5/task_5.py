# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

import random

with open('task_5.txt', 'w') as my_file:
    for el in range(5):
        my_file.write(f'{random.randint(0, 10)} ')

with open('task_5.txt') as my_file:
    nums = my_file.read().split()
    sum = 0
    for num in nums:
        sum += int(num)

print(sum)
