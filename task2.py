"""Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения,город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""


def main(name, sname, day_of_b,city,email, phonenum): # в 27 строке функция принимает именованые аргументы
    data = f"Имя: {name} {sname}, Год {day_of_b}, Город {city}, Email: {email}, Телефон: {phonenum}"
    print(data)
    input("Нажмите любую клавишу для выхода\n")



if __name__ == '__main__':
    fname = input("Введите ваше имя:\n")
    sname = input("Введите вашу фамилию:\n")
    dbirth = input("Введите ваш год рождения:\n")
    city = input("Введите ваш город проживания\n")
    while True:
        email = input("Введите ваш email\n")
        if "@" not in email or len(email)<5:
            input("Вы ввели неверный имейл, нажмите любую клавишу, чтобы продолжить\n"
                  "*имейл должен включать @ и быть не меньше 5 символов!\n")
        elif "@" in email and len(email)>=5:
            break
    mphone = input("Введите ваш номер телефона: \n")
    main(name=fname, sname=sname, day_of_b=dbirth, city=city,email=email,phonenum=mphone)