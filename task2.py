
"""Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк"""


def convertation(seconds):
    sec = seconds % 60
    minetes = (seconds // 60) % 60
    hours = ((seconds // 60) // 60) % 24
    days = (((seconds // 60) // 60) // 24) % 365
    sec = "00"+str(sec)
    minetes = "00"+str(minetes)
    hours = "00"+str(hours)
    print("После конвертации это будет:")
    print(f"Дней: {days} Часов: {hours[-2:]} Минут: {minetes[-2:]} Секунд: {sec[-2:]}")


def main():
    while True:
        seconds = input("Введите количество секунд для конвертации(числом), но можете попытаться и строкой:\n")
        if seconds.isdigit() == True:
            seconds = int(seconds)
            break
    convertation(seconds)


if __name__ == '__main__':
    main()
