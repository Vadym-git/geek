"""Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
(Подсказка: не нумеруйте строки вручную, для этого есть встроенная функция, которой можно передать параметром первое число,
с которого начинать пересчет.)"""


def main():
    some_str = input("Ведите какуюто строку, слова разделяйте пробелами:\n")
    some_list = some_str.split(" ")
    for i in enumerate(some_list, 1):
        """В задании сказано вывести каждое слово с новой строки, потому делаю так как в строке 13 ибо функция 
        enemerate выдает кортеж, что не соответсвует поставленной задаче"""
        print(f"{i[0]}. {i[1][:10]}")


if __name__ == '__main__':
    main()
    input("Нажмите любую клавишу для выхода")