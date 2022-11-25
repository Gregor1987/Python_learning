def view_data(data):
    print(data)


def log_in():
    return input('Введите ваше имя:\n')


def operation_type(message='Выберите способ взаимодействия\n'
                           'Для эскпорта данных нажмите 1\n'
                           'Для импорта данных нажмите 2\n'
                           'Для выхода введите "q"\n'):
    op_type = input(message)
    while op_type != '1' and op_type != '2' and op_type != 'q':
        op_type = operation_type('некорректный выбор, попробуйте еще раз\n')
    return op_type


def export_format(message='Выберите формат для экспорта данных:\n'
                          '1 - вывод в форме строки\n'
                          '2 - вывод в форме визитки\n'):
    exp_form = input(message)
    while exp_form != '1' and exp_form != '2':
        exp_form = export_format('некорректный выбор, попробуйте еще раз\n')
    return exp_form


def input_data():
    family_name = input('введите фамилию:\n')
    name = input('введите имя:\n')
    phone = input('введите номер телефона:\n')
    position = input('введите должность:\n')
    salary = input('введите размер оклада:\n')
    return {'Фамилия': family_name, 'Имя': name, 'Номер телефона': phone, 'Должность': position, 'Оклад': salary}


def search_element():
    data_element = input('выберите элемент для поиска по базе:\n'
                         '1 - поиск по фамилии\n'
                         '2 - поиск по имени\n'
                         '3 - поиск по номеру телефона\n')
    while data_element != '1' and data_element != '2' and data_element != '3':
        data_element = input('некорректный выбор, попробуйте еще раз\n')
    if data_element == '1':
        data_element = 'Фамилия'
        data_output = 'фамилию'
    elif data_element == '2':
        data_element = 'Имя'
        data_output = 'имя'
    else:
        data_element = "Номер телефона"
        data_output = 'номер телефона'
    search_el = input(f'введите {data_output} для поиска в базе\n'
                      'для вывода всей базы введите "all"\n')
    return search_el, data_element
