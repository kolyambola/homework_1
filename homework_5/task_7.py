# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
# словарь (со значением убытков).

import json

firms = {}
firm_count = 0
firm_sum = 0
with open('task_7.txt') as my_file:
    my_file_lines = my_file.readlines()

for line in my_file_lines:
    data = line.split()
    profit = float(data[2]) - float(data[3])
    firms.update({data[0]: profit})
    if profit > 0:
        firm_count += 1
        firm_sum += profit

middle_profit = firm_sum / firm_count
result = [firms, {'middle_profit': middle_profit}]

with open('result.json', 'w', encoding='utf-8') as my_file:
    json.dump(result, my_file)

with open('result.json', encoding='utf-8') as my_file:
    result = json.load(my_file)
    print(result)
