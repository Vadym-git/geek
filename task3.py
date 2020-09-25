"""Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 2.
Считаем 2 + 22 + 222 = 246."""


def some_summa(s):
    n = 2
    stroka = f"{s}"
    while n <= 6:
        stroka = stroka+"+"+stroka[-1]*n
        n = n+1
        print(f"{stroka}={eval(stroka)}")

def main():
    while True:
        digit = input("Введите число которое вы хотите складывать:\n")
        if digit.isdigit() == True:
            digit = int(digit)
            break
    some_summa(digit)
    input("Нажмите любую клавишу для выхода")


if __name__ == '__main__':
    main()