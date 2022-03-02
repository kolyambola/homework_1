# Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
# учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета
# были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по
# нему. Вывести его на экран.

with open('task_6.txt') as my_file:
    my_file_lines = my_file.readlines()

result = {}

for line in my_file_lines:
    data = line.split()
    hours = 0
    for el in data[1:]:
        if el != '-':
            num = '0'
            for i in el:
                if i.isdigit():
                    num += i
                else:
                    break
            hours += int(num)
    result.update({data[0].strip(':'): hours})
print(result)
