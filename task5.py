'''
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationery:
    title = None  # не инициализирую ибо мы ничего не передаем в этот атрибут

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Pen drawing')


class Pencil(Stationery):
    def draw(self):
        print('Pencil drawing')


class Handle(Stationery):
    def draw(self):
        print('Please use the blackboard for drawing')


pen = Pen()

pencil = Pencil()

handle = Handle()

pen.draw()
pencil.draw()
handle.draw()
