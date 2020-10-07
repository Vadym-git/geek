from functools import reduce
"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Подсказка: использовать функцию reduce().
Необходимо получить результат вычисления произведения всех элементов списка.
"""
def mycount(first, sec):
    res = first*sec
    return res


def main():
    mylist = [i for i in range(100,1001)]
    print(reduce(mycount, mylist))

if __name__ == '__main__':
    main()