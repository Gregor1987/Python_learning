import view
import log
import import_data
import export_data


def ees_database(login):
    ops_type = view.operation_type()
    if ops_type == '1':
        search_el, data_el = view.search_element()
        data = export_data.export_output(search_el, view.export_format(), export_data.export_data(), data_el)
        view.view_data(data + '\n')
        log.log(login, 1, search_el, data)
        ees_database(login)
    elif ops_type == '2':
        data = view.input_data()
        import_data.import_data(data)
        log.log(login, 2, data, '')
        view.view_data('Запись внесена\n')
        ees_database(login)
    else:
        view.view_data('До свидания!')
