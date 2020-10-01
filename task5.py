"""Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Исходный набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2]"""

def insert_item(rating, rating_position):
    if len(rating)==0: # проверяем не пустой ли список, если да то сразу вставляем туда элемент без проверки
        rating.append(rating_position)
        return rating
    for i in range(len(rating)):
        if rating_position == rating[i]: # если встретился равный элемент, узнаем сколько таких и в конце вставляем введенный
            n = rating.count(rating[i])
            index = rating.index(rating[i])
            rating.insert(index+n, rating_position) # это сделано, что точно следовать заданию - вставляем именно в конец одинаковых элементов
            return rating
        if rating_position > rating[i]: # если введенная цифра больше н-элемента на его место ставим эту цифру
            rating.insert(i, rating_position)
            return rating



def main():
    rating = []
    while True:
        while True:
            rating_position = input(
                "Введите простое, натуральное, целое число:\nДля выхода введите \"exit\"\n")
            if rating_position.isdigit() == True:
                rating_position = int(rating_position)
                break
            if rating_position == "exit":
                exit()
        my_list = insert_item(rating, rating_position)
        if my_list == None: # если после прохода не выполнилось ни одно условия, знаит элемент меньше всех в списке. Вставляем его в конец
            rating.append(rating_position)
        print(rating)


if __name__ == '__main__':
    main()