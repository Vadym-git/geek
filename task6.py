"""Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя
(для быстроты попробуйте запрашивать все данные разом — "компьютер 20000 5 шт.").
Для скорости можно не реализовывать проверку на корректность всех-всех данных,
но обязательно используйте правильные типы, не сохраняйте все в строки."""

def add_new(staff):
    name_of_staff = input("Введите название вашего товара:\n")
    while True:
        price = input(
            "Введите цену вашего товара:\n")
        if price.isdigit() == True:
            price = int(price)
            break
    while True:
        mount = input(
            "Введите количество:\n")
        if mount.isdigit() == True:
            mount = int(mount)
            break
    type_of_staff = input("Введите единыцы измерения\nПример: шт, кг, литр\n")
    new_staff = (len(staff) + 1, {"name": name_of_staff, "price": price, "mount": mount, "type": type_of_staff})
    staff.append(new_staff)
    print(new_staff)
    return staff

def total(staff):
    names = []
    price = []
    mount = []
    type_of_staff = []
    total_staff = {"name":names , "price": price, "mount": mount, "type": type_of_staff}
    for i in staff:
        name_s= i[1].get("name")
        names.append(name_s)
        price_s = i[1].get("price")
        price.append(price_s)
        mount_s = i[1].get("mount")
        mount.append(mount_s)
        type_s = i[1].get("type")
        type_of_staff.append(type_s)
    print(total_staff)



def main():
    staff = []
    while True:
        choise = input("Смотреть готовую структуру(если она не пустая), нажмите 1\nДобавить товары, нажмите 2\n3 - Выход\n")
        if choise == "1":
            total(staff)
        if choise == "2":
            add_new(staff)
        if choise == "3":
            exit()


if __name__ == '__main__':
    main()