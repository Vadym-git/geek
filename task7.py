'''
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
'''
import json
average_profit = []
total = [{},{}]
with open('helper_task7.txt') as f, open('task7_dump.txt', 'w') as jsdf:
    for i in f:
        kompany = i.strip().split()
        kname = kompany[0]
        profit = int(kompany[1]) - int(kompany[2])
        total[0].update([(kname,profit)])
        if profit>0:
            average_profit.append(profit)
    el = 'average_profit',sum(average_profit)/len(average_profit)
    total[1].update([el])
    json.dump(total,jsdf)
    # print(total)