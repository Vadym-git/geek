'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

with open('helper_task3.txt') as f:
    salary = []
    for i in f:
        i = i.split()
        salary.append(int(i[2]))
        if int(i[2])<20000:
            print(' '.join(i[:2]).title())
average_salary=sum(salary)/len(salary)
print(f'Average salary: {round(average_salary, 2)} £')