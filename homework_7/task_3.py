# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо
# создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
# количеству ячеек клетки (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только
# к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением
# до целого) деление клеток, соответственно.

class Nucleus:
    def __init__(self, sections):
        self.sections = sections

    def __add__(self, other):
        return Nucleus(self.sections + other.sections)

    def __sub__(self, other):
        res = self.sections - other.sections
        if res >= 0:
            return Nucleus(res)
        else:
            return 'Ошибка'

    def __mul__(self, other):
        return Nucleus(self.sections * other.sections)

    def __truediv__(self, other):
        return Nucleus(self.sections // other.sections)

    def make_order(self, count):
        s = ''
        for i in range(self.sections // count):
            s += '*' * count + '\n'
        s += '*' * (self.sections % count) + '\n'
        return s

    def __str__(self):
        return f'{self.sections}'

nucleus_1 = Nucleus(10)
print(nucleus_1.make_order(4))
nucleus_2 = Nucleus(29)
print(nucleus_2.make_order(7))

print(nucleus_1 + nucleus_2)
print(nucleus_1 - nucleus_2)
print(nucleus_2 - nucleus_1)
print(nucleus_1 * nucleus_2)
print(nucleus_1 / nucleus_2)
print(nucleus_2 / nucleus_1)
