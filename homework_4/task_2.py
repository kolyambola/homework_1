# Представлен список чисел. Необходимо вывести элементы исходного списка, значения
# которых больше предыдущего элемента.

list_1 = [2, 6, 4, 1, 1, 18, 55, 25, 28, 13]
list_2 = [el for num, el in enumerate(list_1) if list_1[num - 1] < list_1[num]]

print(f'First list - {list_1}')
print(f'Second list - {list_2}')
