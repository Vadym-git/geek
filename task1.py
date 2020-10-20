'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''


class Data:
    def __init__(self, some_str_data):
        self.str_data = some_str_data

    @classmethod
    def from_str_to_int(cls, date_str):
        some_data = date_str.split('-')
        return some_data

    @staticmethod
    def check_format(date_str):  # 'list' - мне нравится формат списка на выходе. в задании на это ограничения нет
        data = Data.from_str_to_int(date_str)
        '''data = Data.from_str_to_int(date_str) Дает возможность просто ввести данные в заданном формате в виде строки
        или если мы присвоем какую-то дату экземпляру класса
        '''
        for i in data:
            if not i.isdigit():
                raise ValueError(f'{i}; Only integers!')
        if int(data[0]) > 31 or int(data[0]) <= 0:
            raise ValueError(f'Wrong data size: {data[0]}')
        if int(data[1]) > 12 or int(data[1]) <= 0:
            raise ValueError(f'Wrong month size: {data[1]}')
        if len(data[2])<4:
            raise ValueError(f'Wrong month size: {data[2]}')
        return data


a = Data('23-07-1990')
print(Data.from_str_to_int(a.str_data)) # испытываем @classmethod
a.check_format('23-07-1990') # испытываем @staticmethod
