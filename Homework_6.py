# Дан список: ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
# Главное: дополнить числа до двух разрядов нулём!
#
# Решить задачу не создавая новый список (как говорят, in place). Эта задача намного серьёзнее, чем может сначала показаться.


def insert_quotes(some_list, index):
    some_list.insert(index + 1, '"')
    some_list.insert(index - 1, '"')


def modify_line(some_line):
    for i in range(-(len(some_line)), 1):
        if some_line[i].isdigit() and len(some_line[i]) < 2:
            some_line[i] = '0' + some_line[i]
            insert_quotes(some_line, i)
        elif some_line[i].isdigit() and "." not in some_line[i]:
            insert_quotes(some_line, i)
        elif ('+' in some_line[i] or '-' in some_line[i]) and len(some_line[i]) == 2:
            some_line[i] = some_line[i][0] + '0' + some_line[i][1]
            insert_quotes(some_line, i)
        elif '-' in some_line[i]:
            check = False  # этот блок проверяет что элемент списка - это число со знаком, а не местоимение,
            # содержащее знак "-"
            for j in some_line[i]:
                if j.isdigit():
                    check = True
            if check:
                insert_quotes(some_line, i)
    return some_line


def print_line(any_line):
    count = 0
    for i in range(len(any_line) - 1):
        if any_line[i] == '"':
            count += 1
            if count % 2 != 0:
                print(f'{any_line[i]}', end='')
            else:
                print(f'{any_line[i]}', end=' ')
        elif any_line[i].isdigit() or '+' in any_line[i]:
            print(f'{any_line[i]}', end='')
        elif '-' in any_line[i]:
            check = False
            for j in any_line[i]:
                if j.isdigit():
                    check = True
            if check:
                print(f'{any_line[i]}', end='')
            else:
                print(f'{any_line[i]}', end=' ')
        else:
            print(f'{any_line[i]}', end=' ')
    print(f'{any_line[-1]}')


line = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print_line(modify_line(line))

# Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
# Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.

some_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор '
                                                                                                        'аэлита']
for i in range(len(some_list)):
    print(f'Привет, {some_list[i].split()[-1].capitalize()}!')

# Можно ли при этом не создавать новый список?

some_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор '
                                                                                                        'аэлита']
for i in range(len(some_list)):
    print(f'Привет, {some_list[i][some_list[i].rfind(" ") + 1:].capitalize()}!')

# Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).

import random


def print_prices(some_list):
    print_string = ''
    for i in range(len(some_list)):
        if '.' in str(some_list[i]):
            print_string += f'{str(some_list[i])[:str(some_list[i]).find(".")]} руб.'
            if len(str(some_list[i])[str(some_list[i]).find('.') + 1:]) < 2:
                print_string += f' {str(some_list[i])[str(some_list[i]).find(".") + 1:]}0 коп.'
            else:
                print_string += f' {str(some_list[i])[str(some_list[i]).find(".") + 1:]} коп.'
        else:
            print_string += f'{str(some_list[i])[:str(some_list[i]).find(".")]} руб. 00 коп.'
        print_string += ', '
    print(print_string[:-2])


price_list = [round(random.randint(0, 500) + random.random(), 2) for _ in range(random.randint(10, 21))]
print_prices(price_list)

# Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же)

price_list.sort()
print_prices(price_list)

# Создать новый список, содержащий те же цены, но отсортированные по убыванию.

new_price_list = []
for i in range(len(price_list)):
    new_price_list.insert(0, price_list[i])
print_prices(new_price_list)

# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

five_most_expensive = price_list[-5:]
print_prices(five_most_expensive)
