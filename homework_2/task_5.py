# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который
# не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге
# существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.

list_1 = [7, 5, 4, 4, 2, 1]
number = int(input('Введите число '))

inserted = False
for ind, el in enumerate(list_1):
    if number > el:
        list_1.insert(ind, number)
        inserted = True
        break

if not inserted:
    list_1.append(number)

print(list_1)
