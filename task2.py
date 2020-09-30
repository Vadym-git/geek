"""Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Исходные списки можете инициализировать прямо в коде, но обязательно проверьте работоспособность, для пустого списка,
списка из 1 элемента, списка с четным количеством элементов и с нечетным.
(Опционально) Если получится, реализуйте обмен, как функцию."""
new_list = [i for i in range(11)]

def main(some_list):
    if len(some_list) <= 1:
        print(f"Похоже, что ваш список слишком короткий для этой операции. Длина вашего списка: {len(some_list)}")
        return input("Нажмите любую клавишу для выхода")
    if len(some_list)%2 == 0:
        list_len = len(some_list) # меняются элементы только когда индекс списка парный(то есть у нас не будет выхода из индекса списка)
    else: list_len = len(some_list)-1 # аналогично и тут, просто мы до последнего(не парного) индекса не доходим
    for i in range(list_len):
        if i%2 == 0:
            some_list[i], some_list[i+1] = some_list[i+1], some_list[i]
    print(some_list)


if __name__ == '__main__':
    main(new_list)
