# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
# элемента — номер товара и словарь с параметрами, то есть характеристиками товара:
# название, цена, количество, единица измерения. Структуру нужно сформировать программно,
# запросив все данные у пользователя.

products = []
counter = 1
command = ''

while command != 'стоп':
    name = input('Название: ')
    price = input('Цена: ')
    amount = input('Количество: ')
    measure = input('Ед. изм.: ')
    products.append((counter, {'Название': name, 'Цена': price, 'Количество': amount, 'Ед. изм.': measure}))
    counter += 1
    command = input('Напишите "стоп", если хотите завершить ввод: ')
print(products)

dict_1 = {'Название': [], 'Цена': [], 'Количество': [], 'Ед. изм.': []}

for number, dict_2 in products:
    for key, value in dict_2.items():
        dict_1[key].append(value)

for key, value in dict_1.items():
    dict_1[key] = list(set(value))

print(dict_1)
