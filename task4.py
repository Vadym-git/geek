'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
'''


class Car:
    def __init__(self, name, speed=None, color=None, police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = police

    def go(self):
        print('Car started to move')

    def stop(self):
        print('Car stopped')

    def turn(self, direction='ahead'):
        print(f'Car turned {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        self.speed = self.speed - 10
        if self.speed > 60:
            print(f'You drive to fast, your speed is {self.speed}')
        else:
            print(f'Your speed is {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        self.speed = self.speed - 20
        if self.speed > 40:
            print(f'You drive to fast, your speed is {self.speed}')
        else:
            print(f'Your speed is {self.speed}')


class PoliceCar(Car):
    def lits_on(self):
        print('Attention')  # я не придумал ничего лучше как добавить "Внимание" окружающийм и прибавить скорости
        self.speed = self.speed + 20


# Для класса спорт-кар вообще идей нет. Надеюсь можно безе него. В следующем задании сделю все, что там надо будет.

car1 = WorkCar('BMW', speed=100)
car1.show_speed()
