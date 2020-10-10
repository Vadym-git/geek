'''
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''
def some_fun():
    with open('helper_task1.txt', 'w') as mfile:
        for _ in range(0,4):
            some_str = input('Введите какие либо символы, данные:\n')
            mfile.write(f'{some_str}\n')
        input('')

if __name__ == '__main__':
    some_fun()