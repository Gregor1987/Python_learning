import json


def export_data():
    with open('EEs_database.json', 'r') as file:
        return json.load(file)


def export_output(search_element, exp_form, data, data_element):
    exported_data = data["Employees"]
    if search_element == 'all':
        if exp_form == '1':
            export_line = str(exported_data)[1: -2]\
                .replace("{", '')\
                .replace('}, ', ';\n')\
                .replace("'", '')
        else:
            export_line = str(exported_data)[1: -2]\
                .replace(", ", '\n')\
                .replace("{", '')\
                .replace('}', '\n')\
                .replace("'", '')
    else:
        export_line = list(filter(lambda item: item[data_element] == search_element, exported_data))
        if export_line:
            if exp_form == '1':
                export_line = str(export_line)[2: -2].replace("'", '')
            else:
                export_line = str(export_line)[2: -2].replace(', ', '\n').replace("'", '')
        else:
            export_line = 'Такой записи нет'
    return export_line
