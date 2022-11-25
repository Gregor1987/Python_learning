import json
from os.path import isfile


def import_data(data):
    file_name = 'EEs_database.json'
    if isfile(file_name):
        with open(file_name, 'r+') as file:
            file_data = json.load(file)
            file_data["Employees"].append(data)
            file.seek(0)
            json.dump(file_data, file, indent=3, ensure_ascii=False)
    else:
        with open(file_name, 'w') as file:
            file_data = {"Employees": []}
            file_data["Employees"].append(data)
            json.dump(file_data, file, indent=3, ensure_ascii=False)
