# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
# сотрудников.

with open('task_3.txt') as my_file:
    my_file_lines = my_file.readlines()

workers = {}
sum_pay = 0
for i in my_file_lines:
    workers_info = i.split()
    workers.update({workers_info[0]: float(workers_info[1])})
    sum_pay += float(workers_info[1])
middle_pay = sum_pay / len(workers)
print(f'Средний доход сотрудников - {middle_pay:.2f}')

for surname, pay in workers.items():
    if pay < 20000:
        print(f'Сотрудники, имеющие оклад менее 20000: {surname}: {pay}')
