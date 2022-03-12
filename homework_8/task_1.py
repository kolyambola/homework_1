# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        data_list = []
        for i in day_month_year.split():
            if i != '-':
                data_list.append(i)
        return f'{int(data_list[0]):02}.{int(data_list[1]):02}.{int(data_list[2])}'

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2022:
                    return f'Верно'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата: {Data.extract(self.day_month_year)}'

day = Data('9 - 3 - 2022')
print(day)
print(Data.valid(9, 3, 2023))
print(day.valid(32, 6, 2018))
print(Data.valid(9, 13, 1600))
print(day.valid(2, 5, 2019))
print(Data.extract('13 - 11 - 2010'))
print(day.extract('19 - 3 - 1999'))
