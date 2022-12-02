class Person:
    def __init__(self, name, patronymic, family_name, phones):
        self.name = name
        self.patronymic = patronymic
        self.family_name = family_name
        self.phones = dict(phones)

    def get_phone(self):
        if 'private' in self.phones.keys():
            return self.phones['private']
        else:
            return None

    def get_name(self):
        return f'{self.family_name} {self.name} {self.patronymic}'

    def get_work_phone(self):
        if 'work' in self.phones.keys():
            return self.phones['work']
        else:
            return None

    def get_sms_text(self):
        return f'Уважаемый {self.name} {self.patronymic}! Примите участие в нашем ' \
               f'беспроигрышном конкурсе для физических лиц!'


class Company:
    def __init__(self, name, company_type, phones, *args,):
        self.name = name
        self.company_type = company_type
        self.employee = list(args)
        self.phones = dict(phones)

    def get_phone(self):
        if 'contact' in self.phones.keys():
            return self.phones['contact']
        else:
            for i in range(len(self.employee)):
                if self.employee[i].get_work_phone() is not None:
                    break
            return self.employee[i].get_work_phone()

    def get_name(self):
        return str(self.name)

    def get_sms_text(self):
        return f'Для компании {self.name} есть супер предложение! Примите участие в ' \
               f'нашем беспроигрышном конкурсе для {self.company_type}.'


def send_sms(*args):
    receiver_list = list(args)
    for i in range(len(receiver_list)):
        if receiver_list[i].get_phone() is not None:
            print(f'Отправлено СМС на номер {receiver_list[i].get_phone()} с текстом: {receiver_list[i].get_sms_text()}\n')
        else:
            print(f'Не удалось отправить сообщение абоненту: {receiver_list[i].get_name()}.\n')
