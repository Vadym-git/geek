"""Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня."""

def checkin(income,target):
    n = 1
    print(f"{n}-й день, км: {income}")
    while True:
        n = n + 1
        income = income+(income/100)*10
        print(f"{n}-й день, км: {round(income, 2)}")
        if income >= target:
            print(f"Спортсмен пробежал {target} км на {n} день своих тренировок")
            break


def main():
    while True:
        income = input("Введите сколько километров пробежал спортсмен в первый день своих тренировок:\n")
        if income.isdigit() == True:
            income = int(income)
            break
    while True:
        target = input("Введите, сколько километров спортсмен должен пробегать в итоге, его цель:\n")
        if target.isdigit() == True:
            target = int(target)
            break
    if income > target:
        print("У вас странный спортсмен, видимо курит что-то, раз в первый день пробежал больше чем его цель! )))")
    else:
        checkin(income=income,target=target)
    input("Нажмите любую клавишу для выхода")


if __name__ == '__main__':
    main()