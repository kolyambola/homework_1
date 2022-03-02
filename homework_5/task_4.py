# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
# этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

nums = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('task_4.txt') as my_file, open('task_4.1.txt', 'w') as my_file_2:
    my_file_line = my_file.readlines()
    for line in my_file_line:
        i = line.split()
        rus_nums = nums.get(i[0])
        my_file_2.write(f'{line.replace(i[0], rus_nums)}')
