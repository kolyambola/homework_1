# Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.

def my_func(num_1, num_2, num_3):
    if num_1 > num_3 and num_2 > num_3:
        return num_1 + num_2
    elif num_1 > num_2 and num_2 < num_3:
        return num_1 + num_3
    else:
        return num_2 + num_3

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))
print(my_func(num_1, num_2, num_3))
