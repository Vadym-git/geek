from random import randint
'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
with open('helper_task5.txt','w+') as f: # режим записи 'w' ибо в условиях сказанно создать файл програмно
    for i in range(1,100):
        i = randint(0,1000)
        end = ''
        if i %10 == 0: # чтобы не все в одну строку
            end = '\n'
        f.writelines(f'{i} {end}')
    tlist = []
    f.seek(0)
    for k in f.readlines():
        k = k.split()
        k = [int(i) for i in k]
        tlist.extend(k)
    tsum = sum(tlist)
    print(f'Сумма чисел в файле: {tsum}')