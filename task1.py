"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""


def division(num1, num2):
    """Я сложная функция которая делит первый агрумент на второай"""
    try:
        res = num1 / num2
        print(f"Результат: {res}")
    except ZeroDivisionError: # предусматриваем операцию с делением на ноль
        exit_cont = input("Похоже, что вы пытаетесь поделить на ноль, подучите математику,\n"
                          "и нажмите любую клавишу чтобы продолжить\nНаберите \"exit\" для выхода\n")
        if exit_cont == "exit":
            exit()
        main()


def get_data():
    while True:
        number1 = input("Введите пожалуйста первое число:\n")
        if number1.isdigit() == True:
            number1 = int(number1)
            break
    while True:
        number2 = input("Введите пожалуйста второе число:\n")
        if number2.isdigit() == True:
            number2 = int(number2)
            break
    return number1, number2


def main():
    number1, number2 = get_data()
    division(number1, number2) # принимаем два позиционных аргумента, как в задании.
    input("Нажмите любую клавишу на клавиатуре для выхода\n")


if __name__ == '__main__':
    main()
