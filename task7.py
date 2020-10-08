"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24. На вебинаре реализовали похожий пример для чисел Фиббоначи.
"""
import time
n = 5
def for_el_in_fact(n):
    factorial = 1
    print(factorial)
    for i in range(2, n + 1):
        factorial *= i
        yield factorial
    print(f"factorial = {factorial}") # я не понимаю, что тут хотят, чтобы я выводил в задании. Факториал функция считает!
if __name__ == '__main__':
    for i in for_el_in_fact(n):
        print(i)
