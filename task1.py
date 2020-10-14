'''
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
(Для ожидания нескольких секунд можно использовать метод стандартной библиотеки time.sleep())
'''
import time


class TrafficLight:
    _color = 1  # ничего сюда не передаем, потому без инициализации.

    def running(self):
        self.color = 'RED'
        print(f'{self.color}')
        time.sleep(7)
        self.color = 'YELLOW'
        print(f'{self.color}')
        time.sleep(2)
        self.color = 'GREEN'
        print(f'{self.color}')
        time.sleep(2)


tl = TrafficLight()
tl.running()
