'''
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''


class Close:
    def __init__(self, size):
        if not isinstance(size, (int, float)):
            raise TypeError('You can use only digits for "size"')
        self._size = size

    def _change_size(self, size):
        if not isinstance(size, (int, float)):
            raise TypeError('You can use only digits for "size"')
        self._size = size

    def _show_size(self):
        return self._size

    size = property(fget=_show_size, fset=_change_size)


class Coat(Close):
    def consumption(self):
        consumption = (self._size / 6.5 + 0.5)
        return round(consumption, 2)


class Suit(Close):
    def consumption(self):
        consumption = (2 * self._size + 0.3)
        return round(consumption, 2)


a = Coat(34)
b = Suit(28)
print(a.size)
print(b.size)
a.size = 50
b.size = 35
print(a.size)
print(b.size)
print(a.consumption())
print(b.consumption())