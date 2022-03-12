# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivisionZero(Exception):
    def __init__(self, txt):
        self.txt = txt

number_dividend = input('Введите делимое: ')
number_divider = input('Введите делитель: ')

try:
    number_dividend = int(number_dividend)
    number_divider = int(number_divider)
    if number_divider == 0:
        raise DivisionZero('На нуль делить недопустимо')
except ValueError:
    print('Вы ввели не число')
except DivisionZero as error:
    print(error)
else:
    print(number_dividend / number_divider)
