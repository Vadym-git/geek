'''
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
'''


class Cell:
    def __init__(self, cells):
        if not isinstance(cells, int):
            raise TypeError('only integer')
        self._cells = cells

    def __add__(self, other):
        return self._cells + other._cells

    def __sub__(self, other):
        if self._cells <= other._cells:
            raise SyntaxError(f'"{self}" SHOULD BE > than "{other}"')
        return self._cells - other._cells  # выполняем только если А больше Б - условия задания. и тольк так!!!

    def __mul__(self, other):
        return self._cells * other._cells

    def __truediv__(self, other):
        self._total = self._cells / other._cells
        return round(self._total, 0)
        # написано округлить к целому числу но не указанно в какую сторону, потому просто срезаю лишние знаки

    def make_order(self, row):
        if not isinstance(row, int):
            raise SyntaxError('Only int!')
        self._cells = '*' * self._cells  # создаем строку вида *******
        self.total = []
        for i in enumerate(self._cells, 1):  # перебераем и определяем на четность row
            add = i[1]
            if i[0] % row == 0: # если четное row, добавляем нужный символ в строку
                add = add + r'\n'
                self.total.append(add)
                continue
            self.total.append(add)
        self.total = ''.join(self.total)
        if self.total[-1] == 'n':
            return self.total[:-2]
        return self.total


a = Cell(7)
b = Cell(15)
print(b.make_order(5))
