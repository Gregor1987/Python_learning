# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# # num_translate("one")
# "один"
# num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию,
# необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.


def num_translate(number):
    vocabluary = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                  'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if number in vocabluary.keys():
        print(vocabluary[number])
    else:
        print('такого числа нет')


num_translate(input('введите число: '))

# Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# num_translate_adv("One")
# "Один"
# num_translate_adv("two")
# "два"


def num_translate_adv(number):
    vocabluary = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                  'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if number.istitle():
        if number.lower() in vocabluary.keys():
            print(vocabluary[number.lower()].capitalize())
        else:
            print('такого числа нет')
    elif number in vocabluary.keys():
        print(vocabluary[number])
    else:
        print('такого числа нет')


num_translate_adv(input('введите число: '))

# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
#в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
# thesaurus("Иван", "Мария", "Петр", "Илья")
# {
# "И": ["Иван", "Илья"],
# "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки?


def thesaurus(*args):
    some_list = list(args)
    some_dict = {}
    for i in range(len(some_list)):
        if some_list[i][0] in some_dict.keys():
            some_dict[some_list[i][0]].append(some_list[i])
        else:
            some_dict[some_list[i][0]] = [some_list[i]]
    print(some_dict)
# Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?
    print(dict(sorted(some_dict.items())))


thesaurus('Федор', "Иван", "Мария", "Петр", "Илья", 'Митрофан')

# Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и
# возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по
# схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
# thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
# "А": {
# "П": ["Петр Алексеев"]
# },
# "И": {
# "И": ["Илья Иванов"]
# },
# "С": {
# "И": ["Иван Сергеев", "Инна Серова"],
# "А": ["Анна Савельева"]
# }
# }

def get_key(dictionary, value):
    for k, v in dictionary.items():
        if v == value:
            return k


def thesaurus_adv(*args):
    some_list = list(args)
    some_dict = {}
    for i in range(len(some_list)):
        if some_list[i][some_list[i].find(' ') + 1] in some_dict.keys():
            some_dict[some_list[i][some_list[i].find(' ') + 1]].append(some_list[i])
        else:
            some_dict[some_list[i][some_list[i].find(' ') + 1]] = [some_list[i]]
    for i in some_dict.values():
        temp_dict = {}
        for j in range(len(i)):
            if i[j][0] in temp_dict.keys():
                temp_dict[i[j][0]].append(i[j])
            else:
                temp_dict[i[j][0]] = [i[j]]
        some_dict[get_key(some_dict, i)] = temp_dict
    print(some_dict)


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Федор Суворов")

# Как поступить, если потребуется сортировка по ключам?


def thesaurus_adv_sorted(*args):
    some_list = list(args)
    some_dict = {}
    for i in range(len(some_list)):
        if some_list[i][some_list[i].find(' ') + 1] in some_dict.keys():
            some_dict[some_list[i][some_list[i].find(' ') + 1]].append(some_list[i])
        else:
            some_dict[some_list[i][some_list[i].find(' ') + 1]] = [some_list[i]]
    for i in some_dict.values():
        temp_dict = {}
        for j in range(len(i)):
            if i[j][0] in temp_dict.keys():
                temp_dict[i[j][0]].append(i[j])
            else:
                temp_dict[i[j][0]] = [i[j]]
        some_dict[get_key(some_dict, i)] = dict(sorted(temp_dict.items()))  # сортировка вложенных словарей
    print(dict(sorted(some_dict.items())))  # сортировка основного словаря


thesaurus_adv_sorted("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Федор Суворов")
