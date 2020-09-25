"""Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции."""
def max_digit(digits):
    """Я буду делать это задание цыклом for ибо делать его через while не вижу смысла"""
    maxd = digits[0]
    for digit in digits:
        if digit >= maxd:
            maxd = digit
    print(f"Максимальная цифра в этом числе: {maxd}")




def main():
    while True:
        digit = input("Введите число в котором будем находить самую большую цифру\n"
                      "не поленитесь ввести хотя бы 3х или 4х значное число, лучше больше:\n")
        if digit.isdigit() == True:
            digit = str(digit)
            break
    max_digit(digit)
    input("Нажмите любую клавишу для выхода")


if __name__ == '__main__':
    main()