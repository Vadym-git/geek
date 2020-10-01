"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict."""

def check_in_list(number_of_mon):
    months = [12,1,2,3,4,5,6,7,8,9,10,11]
    if number_of_mon in months[0:3]:
        print("Зима")
    elif number_of_mon in months[0:6]:
        print("Весна")
    elif number_of_mon in months[0:9]:
        print("Лето")
    elif number_of_mon in months[0:12]:
        print("Осень")

def check_in_dict(number_of_mon):
    months = {1:"Зима", 2:"Зима", 3:"Весна", 4:"Весна", 5:"Весна", 6:"Лето", 7:"Лето", 8:"Лето", 9:"Осень", 10:"Осень", 11:"Осень", 12:"Зима"}
    print(months.get(number_of_mon))

def main():
    while True:
        type_of_checkin = input("Каким способом будем проверять месяц на вхождение в определенное время года?\n"
                            "Введите 1 - Через <class 'list'>\n"
                            "Введите 2 - Через <class 'dict'>\n")
        if type_of_checkin == "1" or type_of_checkin == "2":
            type_of_checkin = int(type_of_checkin)
            break
    while True:
        month = input("Введите номер месяца для проверки:\n")
        if month.isdigit() == True and month in ["1", "2", "3","4","5","6","7","8","9","10","11","12"]:
            month = int(month)
            break
    if type_of_checkin == 1:
        check_in_list(month)
    elif type_of_checkin == 2:
        check_in_dict(month)



if __name__ == '__main__':
    main()
    input("Нажмите любую клавишу для выхода")