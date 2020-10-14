'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:
    def __init__(self, name, sname, position, wage, bonus=None):
        self.name = name
        self.sname = sname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        fullname = f'{self.name} {self.sname}'.title()
        print(fullname)

    def get_total_income(self):
        totalinc = self._income['wage'] + self._income['bonus']
        print(totalinc)


worker = Position('Vadym', 'Mel', 'Manager assis', 4000, 3000)
worker.get_total_income()
