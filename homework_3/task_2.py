# Выполнить функцию, которая принимает несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Осуществить вывод данных о
# пользователе одной строкой.

def person_info(name, surname, age, city, email, phone):
    print(f'имя - {name}, фамилия - {surname}, год рождения - {age}, город проживания - {city}, email - {email}, телефон - {phone}')

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
age = int(input('Введите год рождения: '))
city = input('Введите город проживания: ')
email = input('Введите email: ')
phone = int(input('Введите телефон: '))
person_info(name=name, surname=surname, age=age, city=city, email=email, phone=phone)
